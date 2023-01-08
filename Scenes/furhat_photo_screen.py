from Scenes.quiz_scene import QuizScene
from .scene_base import SceneBase
import pygame
from Scenes.rps_scene import RPSScene
from Scenes.maze_scene import MazeScene
from Scenes.emotion_scene import EmotionScene
from Scenes.chess_scene import ChessScene
from Scenes.opening_scene import OpeningScene
from Scenes.quiz_scene import QuizScene
from CONSTANTS import WIDTH, HEIGHT
import math

class FurhatPhotoScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.slide = 0
		self.furhat_img = pygame.image.load("furhat.jpeg").convert_alpha()
		self.image_width = self.furhat_img.get_width()
		self.game_hope = None
		self.game_discontent = None
		self.rebellion = None
		self.quiz_anwered = []
		print("New Photo Scene")
		self.font = pygame.font.SysFont(None, 50)
		self.direction = "left"
		self.furhat = furhat

	
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
		
		self.game_discontent , self.game_hope, self.rebellion = game_params["discontent"], game_params["hope"], game_params["rebellion"]


		
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

		hope = self.font.render(f"Hope: {self.game_hope}", True, (0,0,0))
		text_rect = hope.get_rect(topleft=(100, 100))
		WIN.blit(hope, text_rect)

		discontent = self.font.render(f"Discontent: {self.game_discontent}", True, (0,0,0))
		text_rect = discontent.get_rect(topleft=(100, 150))
		WIN.blit(discontent, text_rect)

		rebellion = self.font.render(f"Rebellion: {self.rebellion}", True, (0,0,0))
		text_rect = rebellion.get_rect(topleft=(100, 200))
		WIN.blit(rebellion, text_rect)
