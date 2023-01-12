from .scene_base import SceneBase
# from Scenes.title_screen import TitleScene
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
import math
import rps_mini_game as rps
from time import sleep, time
import os

cwd = os.getcwd()
img_folder = os.path.join(cwd, "images")
font_folder = os.path.join(cwd, "fonts")


class RPSScene(SceneBase):
	def __init__(self, furhat):
		SceneBase.__init__(self)
		self.img = pygame.image.load(os.path.join(img_folder, "rps_photo.png")).convert_alpha()
		self.img = pygame.transform.scale(self.img, (WIDTH, HEIGHT))
		self.winner = None
		self.won = False
		self.wontime = 0
		self.result = None
		self.font = pygame.font.Font('freesansbold.ttf', 200)
		self.game = rps.RPSMiniGame()
		self.game.furhat = furhat
		self.furhat = furhat

		print("New RPS game")

	def ProcessInput(self, events, pressed_keys, game_params):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")

	def Update(self):
		if self.result is None:
			# -1 left
			# +1 right
			self.winner = self.game.play_game()
			# sleep(1.5)
			print("RPS run")
			self.result = ("RPS", self.winner, None, None)
			self.won = True
			self.wontime = time()
			self.furhat.say("Congrats!")
			if self.winner == 1:
				self.furhat.say("Right Player wins!")
			else:
				self.furhat.say("Left Player wins!")


		# else:
		# 	if time() - self.wontime < 10:
		# 		return None


		return self.result

	def Render(self, WIN):
		WIN.fill((255, 255, 255))
		WIN.blit(self.img, (0, 0))

		pleft_score_text = f"{-self.game.pleft_score}"
		pright_score_text = f"{self.game.pright_score}"
		pleft_text = self.font.render(pleft_score_text, True,
										(0, 0, 0))
		pright_text = self.font.render(pright_score_text, True,
										(0, 0, 0))
		vs_text = self.font.render("vs", True,
									(0, 0, 0))

		WIN.blit(pleft_text, pleft_text.get_rect(
			center=(WIDTH//4, 200)))
		WIN.blit(vs_text, pleft_text.get_rect(
			center=(WIDTH//2 - 60, 200)))
		WIN.blit(pright_text, pright_text.get_rect(
			center=(3*WIDTH//4, 200)))
