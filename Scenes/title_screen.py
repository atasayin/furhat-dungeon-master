from .scene_base import SceneBase
from .volunteer_scene import VolunteerScene
from .furhat_photo_screen import FurhatPhotoScene
from .opening_scene import OpeningScene
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
import math
from time import sleep


class TitleScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.PLAY_BUTTON = Button(image=pygame.image.load("play_button.jpeg").convert_alpha(), pos=(WIDTH/2, HEIGHT-200), text_input=None, font=font, base_color=(240, 0, 0), hovering_color=(0,0,0), scale=0.35)
		self.deg = 0
		self.state = "intro"
		self.furhat = furhat
	
	def ProcessInput(self, events, pressed_keys, game_params):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")
				if self.PLAY_BUTTON.checkForInput(mousepos):
					self.SwitchToScene(VolunteerScene(self.furhat))
					# self.SwitchToScene(FurhatPhotoScene(self.furhat))
					# self.SwitchToScene(OpeningScene(self.furhat))

	
	def Update(self):
		self.PLAY_BUTTON = Button(image=None, pos=(WIDTH/2, HEIGHT-200), text_input="Start Game", font=font, base_color=(240, 0, 0), hovering_color=(100,100,100), scale=0.35)
	
	def Render(self, WIN):
		WIN.fill((255, 255, 255))
		mousepos = pygame.mouse.get_pos()
		self.PLAY_BUTTON.changeColor(mousepos)
		self.PLAY_BUTTON.update(WIN)
		self.deg += 0.03
		text = font.render("Furhat the Dungeon Master", True, (0,0,0))
		text_rect = text.get_rect(center=(WIDTH/2, 150  + math.sin(self.deg) * 40))
		WIN.blit(text, text_rect)


