from .scene_base import SceneBase
from .volunteer_scene import VolunteerScene
from .furhat_photo_screen import FurhatPhotoScene
from .opening_scene import OpeningScene
from .maze_scene import MazeScene
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
import math
from time import sleep
import os 

cwd = os.getcwd()
img_folder = os.path.join(cwd, "images")
fonts_folder = os.path.join(os.getcwd(), "fonts")


class TitleScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.PLAY_BUTTON = Button(image=pygame.image.load("play_button.jpeg").convert_alpha(), pos=(WIDTH/2, HEIGHT-200), text_input=None, font=font, base_color=(240, 0, 0), hovering_color=(0,0,0), scale=0.35)
		self.furhat_img = pygame.image.load(os.path.join(img_folder,"furhat.jpeg")).convert_alpha()
		self.furhat_img = pygame.transform.scale(self.furhat_img, (1200*1.50, int(811*1.50)))
		self.deg = 0
		self.font = pygame.font.Font(os.path.join(fonts_folder, "star_wars_oya.ttf"), 50)
		self.font_title = pygame.font.Font(os.path.join(fonts_folder, "star_wars_oya.ttf"), 75)
		self.slide = 0
		self.direction = "left"

		self.state = "intro"
		self.furhat = furhat
	
	def ProcessInput(self, events, pressed_keys, game_params):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")
				if self.PLAY_BUTTON.checkForInput(mousepos):
					# self.SwitchToScene(VolunteerScene(self.furhat))
					self.SwitchToScene(FurhatPhotoScene(self.furhat))
					# self.SwitchToScene(OpeningScene(self.furhat))


	def Update(self):
		self.PLAY_BUTTON = Button(image=None, pos=(WIDTH/2, HEIGHT-200), text_input="Start Game", font=self.font, base_color=(240, 0, 0), hovering_color=(100,100,100), scale=0.35)
	
	def Render(self, WIN):

		if self.slide > 50:
			self.direction = "right"
		elif self.slide < 0:
			self.direction = "left"


		if self.direction == "left":
				self.slide += 0.1
		else: 
				self.slide -= 0.1

		WIN.fill((255, 255, 255))
		WIN.blit(self.furhat_img, (0-self.slide,0))
		mousepos = pygame.mouse.get_pos()
		self.PLAY_BUTTON.changeColor(mousepos)
		self.PLAY_BUTTON.update(WIN)
		self.deg += 0.03
		text = self.font_title.render("Furhat the Dungeon Master", True, (255,255,255))
		text_rect = text.get_rect(center=(WIDTH/2, 150  + math.sin(self.deg) * 40))
		WIN.blit(text, text_rect)


