from .scene_base import SceneBase
# from Scenes.title_screen import TitleScene
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
import math
from RockPaperScissor import play_game
from time import sleep

class RPSScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.img = pygame.image.load("tierlist.png").convert_alpha()
		self.deg = 0
		self.result = None
		self.slide = 0
		print("New RPS game")
	
	def ProcessInput(self, events, pressed_keys):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")
	
	def Update(self):
		if self.result is None:
			self.result = play_game()
			# sleep(1.5)
			print("RPS run")
			# self.result = 0
		
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

