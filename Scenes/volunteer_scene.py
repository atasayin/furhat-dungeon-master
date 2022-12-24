from .scene_base import SceneBase
from .furhat_photo_screen import FurhatPhotoScene
import pygame
from core.furhat_driver import FurhatDriver
from UI_Objects.button import Button
from CONSTANTS import *
import math
from time import sleep


class VolunteerScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.result = None
		self.furhat = furhat
	def ProcessInput(self, events, pressed_keys, game_params):
		self.player1 , self.player2 = game_params["player1"], game_params["player2"]
	
	def Update(self):
		if self.result is None:
			vol1, vol2 = self.furhat.get_volunteer_status(self.player1, self.player2)
			# if vol1 is not None:
			# 	if vol1:
			# 		self.captain = self.player1
			# 		self.assistant = self.player2
			# 		self.player1.role = "Captain"
			# 		self.player2.role = "Assistant"
			# 	else:
			# 		self.assistant = self.player1
			# 		self.captain = self.player2
			# 		self.player2.role = "Captain"
			# 		self.player1.role = "Assistant"
			
			# self.furhat.define_the_roles(self.captain.id, self.assistant.id)
			self.result = ("VOLUNTEER", vol1, vol2, None)
			self.SwitchToScene(FurhatPhotoScene(self.furhat))
			return self.result
	
	def Render(self, WIN):

		WIN.fill((255, 255, 255))
		mousepos = pygame.mouse.get_pos()
		

		text = font.render("Who will be our captain?", True, (0,0,0))
		text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
		WIN.blit(text, text_rect)

