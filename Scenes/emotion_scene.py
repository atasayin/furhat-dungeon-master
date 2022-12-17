import emotion_mini_game as emotion 
from .scene_base import SceneBase
import pygame
from CONSTANTS import *
from time import sleep


class EmotionScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.img = pygame.image.load("emotion_mini_game/balck_gate.jpg").convert_alpha()
		self.deg = 0
		self.result = None
		self.slide = 0
		self.game = emotion.EmotionMiniGame()			
		print("New Emotion game")
	
	def ProcessInput(self, events, pressed_keys, game_params):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")
	
	def Update(self):
		if self.result is None:
			print("Emotion GAME STARTED")
			self.result = self.game.play_game()
			# sleep(1.5)
			#self.result = 0
		return 0

	def Render(self, WIN):
		# For the sake of brevity, the title scene is a blank red screen

		# print(self.result)
		if self.result is None:
			WIN.fill((255, 255, 255))
			WIN.blit(self.img, (0-self.slide,0))
			self.slide += 0.1
		else:
			# self.SwitchToScene(self.main)
			self.result = 0

