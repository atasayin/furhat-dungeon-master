from .scene_base import SceneBase
import pygame
from Scenes.rps_game import RPSScene
from Scenes.maze_scene import MazeScene
from Scenes.chess_scene import ChessScene
from Scenes.emotion_scene import EmotionScene

class FurhatPhotoScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.slide = 0
		self.furhat_img = pygame.image.load("furhat.jpeg").convert_alpha()
		print("New Photo Scene")

	
	def ProcessInput(self, events, pressed_keys):
		if pressed_keys[pygame.K_SPACE]:
			self.SwitchToScene(RPSScene())
		elif pressed_keys[pygame.K_m]:
			self.SwitchToScene(MazeScene())
		elif pressed_keys[pygame.K_c]:
			self.SwitchToScene(ChessScene())
		elif pressed_keys[pygame.K_e]:
			self.SwitchToScene(EmotionScene())

		
	def Update(self):
		# print("update furhat")
		pass
	
	def Render(self, WIN):
		# The game scene is just a blank blue screen 
		self.slide += 0.1
		WIN.fill((255, 255, 255))
		WIN.blit(self.furhat_img, (0-self.slide,0))