import threading
import pygame
from core.furhat_driver import FurhatDriver
from core.player import Player
from core.territory import Territory
from core.turn import Turn
from Util.colored_print import bcolors
pygame.init()

from CONSTANTS import *
import math
from UI_Objects.button import Button
from Scenes.rps_scene import RPSScene
from Scenes.quiz_scene import QuizScene
from Scenes.chess_scene import ChessScene
from Scenes.emotion_scene import EmotionScene
from furhat_remote_api import FurhatRemoteAPI
from Scenes.maze_scene import MazeScene
from Scenes.chess_scene import ChessScene
from Scenes.emotion_scene import EmotionScene
from time import sleep
import time
import random
from Scenes.title_screen import TitleScene
from Scenes.furhat_photo_screen import FurhatPhotoScene
from milestones import MilestoneManager
from tribes import TribeManager


furhat_last_spoke = time.time()


# screen = pygame.display.set_mode((WIDTH, HEIGHT))



FPS = 60
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()

milestone_words = ["milestone", "stone", "mile", "buy", "bye",
					"unlock", "lock", "purchase", "open", "rebellion", "point",
					"rebel", "point", "points"]

aggro_words = ["aggressive", "raid", "let's go", "conquer", "territory",
				"rate", "red", "read", "attack", "chess",'chaz','test','tezz']
# bolumleri ekle
powerup_words = ["power", "up", "powerup", "special", "ability",
				"tribe"]

quiz_words = ["quiz","chris", "negotiation","who is", "trivia", "question"]
protest_words = ["protest", "emotion", "grotesque",'beretta',"princess",'carretas']

maze_words = ["maze", "labyrinth", "lab", "tribe", "approach"]

initial_territory_list = [Territory(name='Dorms',size=20),Territory(name='Henry Ford',size=5),Territory(name='Ömer',size=10),Territory(name='Odeon',size=10),
				  Territory(name='Library',size=8),Territory(name='Social Science',size=6),Territory(name='CASE',size=5),Territory(name='Engineering',size=15),Territory(name='Science',size=12)]
territory_dict = {0:('DORMS','SARMS','DORMITORY','DORMITORIES','BARB','ALARMS','DARMS','DORM'),1:('HENRYFORD','HENRY FORD','HENRY','FORD','HENRY FORD','HEY FART'),2:('OMER','OMAR','AMAR','WALMART','ÖMER'),3:('ODEON','CALL DOWN', 'DOWN','A DOWN','NERO'),
				  4:('LIBRARY','LIB'),5:('SOS','SAUCE','SOCIAL','SOCIAL SCIENCE','HUMANITIES'),6:('CASE','PACE','BUSSINESS'),7:('ENGINEERING','ENG'),8:('SCIENCE','SIGNS','SIGN','SCIEN')}

milestone_types_dict = {"sallyjazz": ["sally", "jazz"], "open gym": ["gym", "jim", "sports", "field"],
									"remove dress code": ["dress", "code", "remove"], "student clubs": ["club", "student"],
									"lower exile": ["exile", "low", "lower", "lover", "conditions"]}
class Game:
	def __init__(self) -> None:
		self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
		self.active_scene = None
		self.hope = 50
		self.discontent = 50
		self.rebellion_points = 1000
		self.furhat = FurhatDriver()
		self.player1, self.player2 = Player(), Player()
		self.captain, self.assistant = None, None
		self.discontent_gain = 1
		self.hope_gain = 1
		#self.assign_user_ids()
		#self.right_player = self.furhat.find_the_player_on_the_right(self.player1.id, self.player2.id)

		self.milestone_manager = MilestoneManager()
		self.turn = Turn()

		self.territory_list= {0:None,1:None,2:None,3:None,4: Territory(name='Library',size=8),5:None,6:None,7:None,8:Territory(name='Science',size=12)}
		self.game_params = {"discontent": self.discontent, "hope": self.hope, "rebellion": self.rebellion_points,
			"player1": self.player1.id, "player2": self.player2.id, "captain": self.captain, "assistant": self.assistant, 
			"discontent_gain": self.discontent_gain, "hope_gain": self.hope_gain}
		self.passive_rp_income = 20
		# furhat.introduce_players((self.player1.id, self.player2.id))
		self.tribe_manager = TribeManager(self.game_params)
		self.milestone_list = self.milestone_manager.unlocked_oneTimes + self.milestone_manager.unlocked_pasifs
		self.milestone_list_initial_list = self.milestone_manager.locked_oneTimes + self.milestone_manager.locked_pasifs
		self.run_game(TitleScene(self.furhat))



	def render_method(self, scene, event, fps):
		clock = pygame.time.Clock()
		while True:
			clock.tick(fps)
			scene.Render(self.WIN)
			pygame.display.flip()

			if event.is_set():
				break


	def run_game(self,starting_scene):

		pygame.display.set_caption("Dungeon Master")
		print(f"{bcolors.OKGREEN}Running Game. Starting Scene: {starting_scene} {bcolors.ENDC}")
		open('quiz_mini_game/AskedQuestions.txt', 'w').close()
		open('chess_mini_game/AskedQuestions.txt', 'w').close()
		open('emotion_mini_game/AskedQuestions.txt', 'w').close()
		self.furhat.look_at_screen()

		try:
			self.furhat.furhat.say(text="Let's Play a game.", blocking=True)
		except Exception:
			print("FURHAT CANNOT BE FOUND")
		change_scene_event = threading.Event()

		# clock = pygame.time.Clock()

		self.active_scene = starting_scene
		render_thread = threading.Thread(target=self.render_method, args=(self.active_scene, change_scene_event, 60), daemon=True)
		render_thread.start()

		update_result = None
		manual_change = False
		
		while self.active_scene != None:
			pressed_keys = pygame.key.get_pressed()
			
			# Event filtering 
			filtered_events = []
			for event in pygame.event.get():
				quit_attempt = False
				if event.type == pygame.QUIT:
					quit_attempt = True
				elif event.type == pygame.KEYDOWN:
					alt_pressed = pressed_keys[pygame.K_LALT] or \
								pressed_keys[pygame.K_RALT]
					if event.key == pygame.K_ESCAPE:
						quit_attempt = True
					elif event.key == pygame.K_F4 and alt_pressed:
						quit_attempt = True
				
				if quit_attempt:
					change_scene_event.set()
					self.active_scene.Terminate()
					pygame.quit()
				else:
					filtered_events.append(event)

			game_params = {"discontent": self.discontent, "hope": self.hope, "rebellion": self.rebellion_points,
			"player1": self.player1.id, "player2": self.player2.id, "captain": self.captain, "assistant": self.assistant, 
			"discontent_gain": self.discontent_gain, "hope_gain": self.hope_gain,"territory_list": self.territory_list,
			"milestone_list": self.milestone_list, "initial_territory": initial_territory_list, 'initial_milestone': self.milestone_list_initial_list}

			self.active_scene.ProcessInput(filtered_events, pressed_keys, game_params)

			if type(self.active_scene) == FurhatPhotoScene:
				self.manage_turn()

			print(f"{bcolors.BOLD}Current parameters: {self.hope}, {self.discontent}, {self.rebellion_points} {bcolors.ENDC}")
			if update_result is None:
				sleep(0.05)
				update_result = self.active_scene.Update()

			if update_result is not None:
				# resulta bakarak skorlari guncelleme

				return_to_furhat = self.handle_results(update_result)

				update_result = None
				self.wrap_up_turn()
				if return_to_furhat:
					self.active_scene.next = FurhatPhotoScene(self.furhat)

				manual_change = True

				# self.active_scene = FurhatPhotoScene()
				print(f"{bcolors.UNDERLINE}NEXT SCENE when switching back to furhat: {self.active_scene.next} {bcolors.ENDC}")

			if self.turn.turn_type == "milestone" or self.turn.turn_type == "powerup" :
				self.wrap_up_turn()


			if (self.active_scene != self.active_scene.next) or manual_change:
				manual_change = False
				print(f"{bcolors.OKBLUE}SCENE CHANGE from {self.active_scene} to {self.active_scene.next} {bcolors.ENDC}")
				change_scene_event.set()
				render_thread.join()

				change_scene_event = threading.Event()
				render_thread = threading.Thread(target=self.render_method, args=(self.active_scene.next, change_scene_event, 60), daemon=True)
				render_thread.start()

			self.active_scene = self.active_scene.next

	def assign_user_ids(self):
		ids = None
		while ids is None:
			ids = self.furhat.get_user_ids()    
			if ids is None:
				txts = ["Where are you?", "Are you coming?", "I do not see you"]
				ind = random.randint(0,2)
				self.furhat.furhat.say(text=txts[ind]) 
				time.sleep(5)
			else:
				self.player1.id, self.player2.id = ids
				self.furhat.furhat.say(text="Welcome players.")


	def handle_results(self, update_result):

		return_to_furhat = True
		print(f"Update Result: {update_result}")
		if update_result[0] == "VOLUNTEER":
			vol1, vol2 = update_result[1:3]
			if vol1 is not None:
				if vol1 and not vol2:
					self.captain = self.player1
					self.assistant = self.player2
					self.player1.role = "Captain"
					self.player2.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)

				elif vol2 and not vol1:
					self.assistant = self.player1
					self.captain = self.player2
					self.player2.role = "Captain"
					self.player1.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)

				else:
					return_to_furhat = False
					self.active_scene.SwitchToScene(RPSScene(self.furhat))
					update_result = None

		elif update_result[0] == "RPS":
			print("RPS result.")
			#  right player wins
			if update_result[1] == 1:
				if self.right_player == self.player1.id:
					self.captain = self.player1
					self.assistant = self.player2
					self.player1.role = "Captain"
					self.player2.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)
				else:
					self.captain = self.player2
					self.assistant = self.player1
					self.player2.role = "Captain"
					self.player1.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)

			# left player wins
			else:
				if self.right_player == self.player1.id:
					self.captain = self.player2
					self.assistant = self.player1
					self.player2.role = "Captain"
					self.player1.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)
				else:
					self.captain = self.player1
					self.assistant = self.player2
					self.player1.role = "Captain"
					self.player2.role = "Assistant"
					self.furhat.define_the_roles(self.captain.id, self.assistant.id)
		
		elif update_result[0] == "CHESS":
			self.turn.success = random.uniform(0,1) < update_result[1]
			self.turn.hope_change = 10 if self.turn.success else -10
			self.turn.discontent_change = 10 if self.turn.success else -10

			
		elif update_result[0] == "QUIZ":
			# 0, 1, 2 ---> number of correct answers
			success = update_result[1]
			self.turn.hope_change = (success - 1) * 10
			self.turn.discontent_change = (1 - success) * 5
			self.turn.rebellion_point_change = success * 20
	
		elif update_result[0] == "MAZE":
			self.turn.success = update_result[1]
      
		elif update_result[0] == "EMOTION":
			success = update_result[1]
			self.turn.hope_change = (success - 0.5) * 10
			self.turn.discontent_change = (0.5 - success) * 5
			self.turn.rebellion_point_change = success * 20

		return return_to_furhat

	def manage_turn(self):
		selection = ""
		self.furhat.ask_turns()
		answer = self.furhat.ask_question().split()
		print(f"Answer: {answer}")
		for word in answer:
			if word in aggro_words:
				selection = "aggro"
			elif word in milestone_words:
				selection = "milestone"
			elif word in powerup_words:
				selection = "powerup"
			elif word in quiz_words:
				selection = "quiz"
			elif word in maze_words:
				selection = "maze"
			elif word in protest_words:
				selection = "protest"
			elif word == "cool":
				selection = "cool"

		print(f"Move Selection: {selection}")

		if selection == "passive":
			ans = self.furhat.ask_question("Which passive move would you prefer?").split()
			# change selection to specific passive type
			for word in ans: 
				if word in protest_words:
					selection = "protest"
				elif word in quiz_words:
					selection = "quiz"
				elif word in maze_words:
					selection = "maze"
					
		if selection == "aggro":

			print("TERRITORY LIST1 : ", self.territory_list)
			self.chess_turn()
			print("TERRITORY LIST2 : ", self.territory_list)

			# saldirdigi yeri turn'e kaydet
		elif selection == "milestone":
			# ask which milestone
			self.turn.turn_type = "milestone"
			selected_milestone = self.furhat.ask_question("Which milestone do you want to unlock?").split()
			# ['Lower Exile', 'Open GYM', 'Remove Dresscode','Salicaz', 'Student Clubs']
			self.turn.milestone_requested = "sallyjazz"

			for word in selected_milestone:
				for key, value in milestone_types_dict.items():
					if word in value:
						self.turn.milestone_requested = key

			print(f"{bcolors.HEADER} Selected milestone {selected_milestone}, {self.turn.milestone_requested} {bcolors.ENDC}")
			
			# check if already bought
			if not self.milestone_manager.is_already_bought(self.turn.milestone_requested):
				print("MILESOTNE INITAL LIST ",self.milestone_list_initial_list)
				if self.milestone_manager.is_money_enough(self.turn.milestone_requested, self.rebellion_points):
					cost = self.milestone_manager.buy_milestone(self.turn.milestone_requested)
					self.turn.rebellion_point_change = -cost
					self.furhat.say(f"You successfully bought the {self.turn.milestone_requested}!")
					self.furhat.furhat.gesture(name="Wink")
					self.milestone_list = self.milestone_manager.unlocked_oneTimes + self.milestone_manager.unlocked_pasifs
					self.milestone_list_initial_list = self.milestone_manager.locked_oneTimes + self.milestone_manager.locked_pasifs
				else:
					self.furhat.say("My G you are broke")
					self.turn.turn_type = None
			else:
				self.furhat.say(f"You have already unlocked {self.turn.milestone_requested}!")
				self.turn.turn_type = None
			print("MILESOTNE NEW INITAL LIST ", self.milestone_list_initial_list)

		elif selection == "cool":
			self.furhat.shaka()
				
		elif selection == "powerup":
			self.turn.turn_type = "powerup"
			# ! ash which power
			#powerup_requested = self.furhat.ask_question(f"Lets Power up!")
			powerup_requested = "comp"
			power_up = self.tribe_manager.find_unused_powerup_tribe(powerup_requested)

			if power_up:
				power_up.use_powerup_tribe(power_up)
			else:
				# ! POWER UP YOK VEYA YANLIŞ ANLAMA??	
				self.furhat.say(f"You don't have the {powerup_requested} powerup")
		
		elif selection == "maze":
			# gittigi yeri turn'e kaydet
			# ! ash which tribe
			#maze_destination = self.furhat.ask_question(f"Which tribe do you want to go?")
			maze_destination = "comp"
			if not self.tribe_manager.is_already_conquered(maze_destination):
				self.turn.turn_type = "maze"
				self.turn.maze_destination = maze_destination
				self.active_scene.SwitchToScene(MazeScene(self.furhat))
				#self.active_scene.SwitchToScene(MazeScene(self.furhat,self.turn.maze_destination))
			else:
				self.turn.turn_type = None
				self.turn.maze_destination = None 
				self.furhat.say(f"You have already conquered {self.turn.maze_destination} tribe!")
			
		elif selection == "protest":
			self.turn.turn_type = "regular"
			self.active_scene.SwitchToScene(EmotionScene(self.furhat))

		elif selection == "quiz":
			self.turn.turn_type = "regular"
			self.active_scene.SwitchToScene(QuizScene(self.furhat))

		print(" UNLOCKED: ", self.milestone_manager.unlocked_oneTimes)
		print(" UNLOCKED: ", self.milestone_manager.unlocked_pasifs)

		
	def wrap_up_turn(self):
		if self.turn.turn_type == "regular":
			hope, dis, reb = self.turn.get_changes()
			self.hope += hope
			self.discontent += dis
			self.rebellion_points += reb

		elif self.turn.turn_type == "maze":
			if self.turn.success:
				tribe = self.tribe_manager.conquer_tribe(self.turn.maze_destination)
				
		elif self.turn.turn_type == "chess":
			print("IN WRAP UP TURN SUCCESS ",self.turn.success )
			if self.turn.success:
				# territory'i alip ekle
				territory = initial_territory_list[self.turn.attack_territory]
				territory.conquer()
				print("CONQUERED TERRITORY IS ", initial_territory_list[self.turn.attack_territory].name)
				initial_territory_list[self.turn.attack_territory] = None
				self.territory_list[self.turn.attack_territory] = territory
				print("NEW TERITTORY LIST IS ",self.territory_list )
				self.turn.rebellion_point_change = territory.generate_passif_income(self.territory_list)
				self.rebellion_points += self.turn.rebellion_point_change
				self.passive_rp_income += territory.passive_generation
				print(f"TERRITORY PASSIVE {territory.passive_generation}")

			hope, dis, reb = self.turn.get_changes()
			self.hope += hope
			self.discontent += dis
			self.rebellion_points += reb

		elif self.turn.turn_type == "milestone":
			self.rebellion_points += self.turn.rebellion_point_change

		# Milestone and Territory passive skills
		if self.turn.turn_type is not None:
			print(f"Current passive income: {self.passive_rp_income}")
			self.rebellion_points += self.passive_rp_income

		self.sanity_check_for_hope_and_discontent()	
		self.turn.reset_turn()


	def chess_turn(self):
			self.turn.turn_type = "chess"
			attempt = 3
			flag = 0
			while attempt > 0 and  flag != 1:
				print("FLAG ", flag)
				attempt = attempt - 1
				print("attempt ", attempt)
				if flag == 0:
					territory_selection = self.furhat.ask_question(text='WHICH TERRITORY do YOU WANT TO ATTACK')
				elif flag == 2:
					territory_selection = self.furhat.ask_question(text=f'{territory_selection} is already yours please pick another territory to attack')

				territory_selection = territory_selection.upper()
				print("territory_selection is ", territory_selection)
				try:
					for index, value in territory_dict.items():
						if flag ==1:
							break
						for val in value:
							if flag == 1:
								break
							if val in territory_selection:
								print("IN IF ",self.territory_list)
								print("IN I 3 ",  self.territory_list[index])
								if self.territory_list[index] is None:
									self.turn.attack_territory = index
									print("ATTACK INDEX IS ", index)
									flag = 1
									self.furhat.say(
										"ALSO KEEP IN MIND THAT WHILE YOU GO ON A QUEST TO CONQUER YOUR MIGHT GET ATTACKED")
									break
								elif self.territory_list[index] is not None:
									flag = 2
									break

				except:
					self.turn.success = False



			territory_lose_prob = random.uniform(0, 1)
			if territory_lose_prob > 0.7:
				self.furhat.say("IT SEEMS THERE IS AN ATTACK ON YOUR TERRITORIES")
				range_of_territory = len(self.territory_list)
				number =random.randint(0,range_of_territory)
				print("LOST TERITTORY IS  ",number,self.territory_list.get(number))
				try:
					while self.territory_list.get(number) is None:
						number = random.randint(0, range_of_territory)
					lost_ter = self.territory_list.get(number)
					self.furhat.say(f"WHILE you go to {initial_territory_list[self.turn.attack_territory].name} to conquer it, your {lost_ter.name} was lost ")
					self.furhat.say(f"BUT DO NOT LOSE HOPE, YOU CAN STILL TRY TO CONQUER  {initial_territory_list[self.turn.attack_territory].name} ")
					self.territory_list = lost_ter.losing_territory(self.territory_list,number)
					print("SELF TERITTORY LIST 3 AFTER LOST ", self.territory_list)
				except:
					print("YOU DO NOT HAVE TERRITORY TO LOSE")
			if flag == 1:
				self.active_scene.SwitchToScene(ChessScene(self.furhat))
			if flag == 0 or flag == 2:
				self.turn.success = False


	def sanity_check_for_hope_and_discontent(self):
		self.hope = min(self.hope, 100)
		self.discontent = max(self.discontent, 0)

Game()