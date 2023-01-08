import threading
import pygame
from core.furhat_driver import FurhatDriver
from core.player import Player
from core.territory import Territory
from core.turn import Turn
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
				"rate", "red", "read", "attack", "chess"]
# bolumleri ekle
powerup_words = ["power", "up", "powerup", "special", "ability",
				"tribe"]


quiz_words = ["quiz", "negotiation","who is", "trivia", "question"]
protest_words = ["protest", "emotion", "grotesque",'beretta',"princess"]

maze_words = ["maze", "labyrinth", "lab", "tribe", "approach"]

initial_territory_list = [Territory(name='Dorms',size=20),Territory(name='Henry Ford',size=5),Territory(name='Ömer',size=10),Territory(name='Odeon',size=10),
				  Territory(name='Library',size=8),Territory(name='SOS',size=6),Territory(name='CASE',size=5),Territory(name='ENGINEERING',size=15),
				  Territory(name='SNA',size=20),Territory(name='SCIENCE',size=12)]
territory_dict = {0:('DORMS','DORMITORY'),1:('HENRYFORD','HENRY FORD','HENRY','FORD','HENRY FORD','HEY FART'),2:('OMER','ÖMER'),3:('ODEON','NERO'),
				  4:('LIBRARY','LIB'),5:('SOS','SOCIAL','SOCIAL SCIENCE','HUMANITIES'),6:('CASE','BUSSINESS'),7:('ENGINEERING','ENG'),8:('SNA','SNAA'),9:('SCIENCE','SIGNS','SIGN','SCIEN')}

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
		self.passive_rp_income = 20
		self.territory_list= []
		self.game_params = {"discontent": self.discontent, "hope": self.hope, "rebellion": self.rebellion_points,
			"player1": self.player1.id, "player2": self.player2.id, "captain": self.captain, "assistant": self.assistant, 
			"discontent_gain": self.discontent_gain, "hope_gain": self.hope_gain}
		# furhat.introduce_players((self.player1.id, self.player2.id))
		self.tribe_manager = TribeManager(self.game_params)
	   

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
		print("running")
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
			"discontent_gain": self.discontent_gain, "hope_gain": self.hope_gain}

			self.active_scene.ProcessInput(filtered_events, pressed_keys, game_params)

			if type(self.active_scene) == FurhatPhotoScene:
				self.manage_turn()

			print(f"Current parameters: {self.hope}, {self.discontent}, {self.rebellion_points}")
			if update_result is None:
				sleep(0.05)
				# print(f"UPDATE YERI : {self.active_scene}")
				update_result = self.active_scene.Update()
			# self.active_scene.SwitchToScene(TitleScene())
			# self.active_scene.Render(screen)
			
			if update_result is not None:
				# resulta bakarak skorlari guncelleme

				return_to_furhat = self.handle_results(update_result)

				update_result = None
				if return_to_furhat:
					self.active_scene.next = FurhatPhotoScene(self.furhat)

				manual_change = True

				# self.active_scene = FurhatPhotoScene()
				print(f" NEXT SCENE when switch to furhat: {self.active_scene.next}")
			self.wrap_up_turn()
			
			if (self.active_scene != self.active_scene.next) or manual_change:
				manual_change = False
				print(f"SCENE CHANGE from {self.active_scene} to {self.active_scene.next}")
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
		print(update_result)
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
			if random.uniform(0,1) < update_result[1]:
				self.turn.success = True
			else: 
				self.turn.success = False

			
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
		selection = "passive"
		self.furhat.ask_turns()
		answer = self.furhat.ask_question().split()
		print(answer)
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

		print(selection)

		if selection == "passive":
			self.furhat.ask_question()
			# change selection to specific passive type
			pass
		elif selection == "aggro":
			self.turn.turn_type = "chess"
			attempt = 2
			flag = False
			while attempt > 0 and not flag:
				attempt = attempt -1
				territory_selection = self.furhat.ask_question(text='WHICH TERRITORY DO YOU WANT TO ATTACK?')
				territory_selection = territory_selection.upper()
				#  check if territory is already taken
				print("territory_selection is ", territory_selection)
				try:
					for index, value in territory_dict.items():
						for val in value:
							if val in territory_selection:
								self.turn.attack_territory = index
								#self.turn.success = True
								flag = True
								break
				except:
					self.turn.success = False
			self.active_scene.SwitchToScene(ChessScene(self.furhat))
			if flag:
				self.turn.success = True
			else:
				self.turn.success = False

			# saldirdigi yeri turn'e kaydet
		elif selection == "milestone":
			# ask which milestone
			self.turn.turn_type = "milestone"
			self.turn.milestone_requested = "sallyjazz"
			# check if already bought
			if not self.milestone_manager.is_already_bought(self.turn.milestone_requested):
				if self.milestone_manager.is_money_enough(self.turn.milestone_requested, self.rebellion_points):
					cost = self.milestone_manager.buy_milestone(self.turn.milestone_requested)
					self.turn.rebellion_point_change = -cost
					self.furhat.say(f"You successfully bought the {self.turn.milestone_requested}!")
					self.furhat.furhat.gesture(name="Wink")
				else:
					self.furhat.say("My G you are broke")
					self.turn.turn_type = None
			else:
				self.furhat.say(f"You have already unlocked {self.turn.milestone_requested}!")
				self.turn.turn_type = None
				
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
			if self.turn.success:
				# territory'i alip ekle
				territory = initial_territory_list[self.turn.attack_territory]
				territory.conquer()
				initial_territory_list[self.turn.attack_territory] = None
				self.territory_list.append(territory)
				print(f"TERRITORY PASSIVE {territory.passive_generation}")
				self.passive_rp_income += territory.passive_generation

		elif self.turn.turn_type == "milestone":
			self.rebellion_points += self.turn.rebellion_point_change

		# Milestone and Territory passive skills
		if self.turn.turn_type is not None:
			print(f"Current passive income: {self.passive_rp_income}")
			self.rebellion_points += self.passive_rp_income

		self.sanity_check_for_hope_and_discontent()	
		self.turn.reset_turn()

	def sanity_check_for_hope_and_discontent(self):
		self.hope = min(self.hope, 100)
		self.discontent = max(self.discontent, 0)
Game()