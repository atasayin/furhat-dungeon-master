from Scenes.quiz_scene import QuizScene
from .scene_base import SceneBase
import pygame
from Scenes.rps_scene import RPSScene
from Scenes.maze_scene import MazeScene
from Scenes.emotion_scene import EmotionScene
from Scenes.chess_scene import ChessScene
# from Scenes.opening_scene import OpeningScene
from Scenes.quiz_scene import QuizScene
from CONSTANTS import WIDTH, HEIGHT
import math
import os
cwd = os.getcwd()
img_folder = os.path.join(cwd, "images")
font_folder = os.path.join(cwd, "fonts")
class FurhatPhotoScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.slide = 0
		self.furhat_img = pygame.image.load(os.path.join(img_folder,"koc_nice.jpeg")).convert_alpha()
		self.furhat_img = pygame.transform.scale(self.furhat_img, (4096*0.5, int(2160*0.5)))
		self.image_width = self.furhat_img.get_width()
		self.game_hope = None
		self.game_discontent = None
		self.rebellion = None
		self.quiz_anwered = []
		print("New Photo Scene")
		self.font = pygame.font.Font(os.path.join(font_folder, "star_wars_oya.ttf"), 30)
		self.font_small = pygame.font.Font(os.path.join(font_folder, "star_wars_oya.ttf"), 20)
		self.font_large = pygame.font.Font(os.path.join(font_folder, "star_wars_oya.ttf"), 40)
		
		self.direction = "left"
		self.furhat = furhat
		self.rebellion = None
		self.milestone_list = None
		self.initial_territory = None
		self.territory_list = None
		self.territory_name_list = []
		self.milestone_name_list = []
		self.initial_territory_name = []
		self.initial_milestone_list = []
		self.initial_milestone_name = []


	def ProcessInput(self, events, pressed_keys, game_params):
		if pressed_keys[pygame.K_SPACE]:
			self.SwitchToScene(RPSScene(self.furhat))
		elif pressed_keys[pygame.K_m]:
			self.SwitchToScene(MazeScene(self.furhat))
		elif pressed_keys[pygame.K_c]:
			self.SwitchToScene(ChessScene(self.furhat))
		elif pressed_keys[pygame.K_e]:
			self.SwitchToScene(EmotionScene(self.furhat))
		elif pressed_keys[pygame.K_o]:
			self.SwitchToScene(OpeningScene(self.furhat))
		elif pressed_keys[pygame.K_a]:
			self.SwitchToScene(QuizScene(self.furhat,self.quiz_anwered))
		print(game_params)
		self.game_discontent , self.game_hope, self.rebellion, self.territory_list,self.milestone_list, self.initial_territory, self.initial_milestone_list  = game_params["discontent"], game_params["hope"],\
																																						  game_params["rebellion"], game_params['territory_list'],\
																																						  game_params['milestone_list'], game_params['initial_territory'], \
																																							   game_params['initial_milestone']
		for ter in self.territory_list.values():
			if ter != None and ter.name not in self.territory_name_list:
				self.territory_name_list.append(ter.name)

		for ter in self.initial_territory:
			if ter != None and ter.name not in self.territory_name_list and ter.name not in self.initial_territory_name:
				self.initial_territory_name.append(ter.name)

		for mil in self.milestone_list:
			if mil != None and mil.name not in self.milestone_name_list:
				self.milestone_name_list.append(mil.name)

		for mil in self.initial_milestone_list:
			if mil != None and mil.name not in self.initial_milestone_name:
				self.initial_milestone_name.append(mil.name)

		for mil in self.initial_milestone_name:
			if mil != None and mil in self.milestone_name_list:
				self.initial_milestone_name.remove(mil)

		print("milestone_name_list MILESTONE LIST ",self.milestone_name_list)
		print("INITAL MILESTONE LIST ",self.initial_milestone_name)
	def Update(self):
		pass
	
	def Render(self, WIN):
		# The game scene is just a blank blue screen 

		# if self.slide < (WIDTH - self.image_width) or self.slide < 0:
		if self.slide > 100:
			self.direction = "right"
		elif self.slide < 0:
			self.direction = "left"


		if self.direction == "left":
				self.slide += 0.1
		else: 
				self.slide -= 0.1

		WIN.fill((255, 255, 255))
		WIN.blit(self.furhat_img, (0-self.slide,0))

		hope = self.font_large.render(f"Hope: {self.game_hope}", True, (255,10,0))
		text_rect = hope.get_rect(topleft=(100, 50))
		WIN.blit(hope, text_rect)

		discontent = self.font_large.render(f"Discontent: {self.game_discontent}", True, (255,10,0))
		text_rect = discontent.get_rect(topleft=(100, 100))
		WIN.blit(discontent, text_rect)

		rebellion = self.font_large.render(f"Rebellion: {self.rebellion}", True, (255,10,0))
		text_rect = rebellion.get_rect(topleft=(100, 150))
		WIN.blit(rebellion, text_rect)

		territory = self.font_large.render("Your Territories Are: ", True, (255, 255, 255))
		text_rect = territory.get_rect(topleft=(100, 250))
		WIN.blit(territory, text_rect)

		territory = self.font.render("Territories to Conquer: ", True, (255, 255, 255))
		text_rect = territory.get_rect(topleft=(50, 550))
		WIN.blit(territory, text_rect)

		territory = self.font_large.render("Your Milestones Are: ", True, (255, 255, 255))
		text_rect = territory.get_rect(topleft=(750, 100))
		WIN.blit(territory, text_rect)

		territory = self.font.render("Milestones To Buy: ", True, (255, 255, 255))
		text_rect = territory.get_rect(topleft=(720, 550))
		WIN.blit(territory, text_rect)

		# item_count = 1
		# for item in self.territory_name_list:
		# 	territory = self.font.render(f"{item}", True, (200, 200, 200))
		# 	text_rect = territory.get_rect(topleft=(100, 280+35*item_count))
		# 	WIN.blit(territory, text_rect)
		# 	item_count +=1

		item_count = 1
		for item2 in self.territory_name_list:
			y_coord = 600 + 35 * item_count
			x_coord = 100 * item_count +20
			if item_count % 2 == 1:
				territory = self.font.render(f"{item2}", True, (200, 200, 200))
				text_rect = territory.get_rect(topleft=(100, 280 + 25* item_count))
				WIN.blit(territory, text_rect)
			elif item_count % 2 ==0:
				territory = self.font.render(f"{item2}", True, (200, 200, 200))
				text_rect = territory.get_rect(topleft=(350, 280+ 25 * (item_count - 1)))
				WIN.blit(territory, text_rect)
			item_count +=1

		item_count = 1
		for item2 in self.initial_territory_name:
			y_coord = 600 + 35 * item_count
			x_coord = 100 * item_count +20
			if item_count % 2 ==0:
				territory = self.font.render(f"{item2}", True, (200, 200, 200))
				text_rect = territory.get_rect(topleft=(50, y_coord))
				WIN.blit(territory, text_rect)
			elif item_count % 2 ==1:
				if item_count == 1:
					territory = self.font.render(f"{item2}", True, (200, 200, 200))
					text_rect = territory.get_rect(topleft=(50, 600))
					WIN.blit(territory, text_rect)
				else:
					territory = self.font.render(f"{item2}", True, (200, 200, 200))
					text_rect = territory.get_rect(topleft=(350, 600 + 35 * (item_count-1)))
					WIN.blit(territory, text_rect)

			item_count += 1

		item_count_mile = 1
		for mile in self.milestone_name_list:
			mile = self.font.render(f"{mile}", True, (200, 200, 200))
			text_rect = mile.get_rect(topleft=(750, 120+30*item_count_mile))
			WIN.blit(mile, text_rect)
			item_count_mile +=1

		item_count = 1
		for item3 in self.initial_milestone_name:
			y_coord = 600 + 35 * item_count
			x_coord = 600 * item_count + 20
			if item_count % 2 == 0:
				mile = self.font.render(f"{item3}", True, (200, 200, 200))
				text_rect = mile.get_rect(topleft=(720, y_coord))
				WIN.blit(mile, text_rect)
			elif item_count % 2 == 1:
				if item_count == 1:
					mile = self.font.render(f"{item3}", True, (200, 200, 200))
					text_rect = mile.get_rect(topleft=(720, 600))
					WIN.blit(mile, text_rect)
				else:
					mile = self.font.render(f"{item3}", True, (200, 200, 200))
					text_rect = mile.get_rect(topleft=(720 + 400, 600 + 35 * (item_count - 1)))
					WIN.blit(mile, text_rect)

			item_count += 1
