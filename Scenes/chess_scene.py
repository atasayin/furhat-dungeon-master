import chess_mini_game as chess 
from .scene_base import SceneBase
import pygame
from CONSTANTS import *
from time import sleep


class ChessScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.img = pygame.image.load("rps_mini_game/rock.jpeg").convert_alpha()
		self.deg = 0
		self.result = None
		self.slide = 0
		self.font = pygame.font.Font('freesansbold.ttf', 20)
		self.game = chess.ChessMiniGame(self)			
		print("New CHESS game")
	
	def ProcessInput(self, events, pressed_keys, game_params):
		mousepos = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK: ", end="")
	
	def Update(self):
		if self.result is None:
			print("CHESS GAME STARTED")
			self.result = self.game.play_game()
			# sleep(1.5)
			#self.result = 0
		return 0

	def Render(self, WIN):
		# For the sake of brevity, the title scene is a blank red screen

		# print(self.result)
		if self.result is None:
			WIN.fill((255, 255, 255))
			WIN.blit(self.img, (0, 0))
			win_text = 'WIN COUNT:'
			pwin_text = f"{self.game.win_count}"
			attempt_text = 'Attempt COUNT:'
			pattempt_text = f"{self.game.attempt_count}"
			life_text = 'Life COUNT:'
			plife_text = f"{self.game.life_count}"
			
			pwin_text = self.font.render(pwin_text, True,
										  (0, 0, 0))
			win_text = self.font.render(win_text, True,
										  (0, 0, 0))
			pattempt_text = self.font.render(pattempt_text, True,
										   (0, 0, 0))
			attempt_text = self.font.render(attempt_text, True,
										   (0, 0, 0))
			plife_text = self.font.render(plife_text, True,
										   (0, 0, 0))
			life_text = self.font.render(life_text, True,
										   (0, 0, 0))

			WIN.blit(win_text, win_text.get_rect(
				center=((WIDTH//12)-200, HEIGHT//12)))
			WIN.blit(pwin_text, pwin_text.get_rect(
				center=(WIDTH//12, HEIGHT//12)))
			WIN.blit(attempt_text, attempt_text.get_rect(
				center=((WIDTH//12) -200, HEIGHT//8)))
			WIN.blit(pattempt_text, pattempt_text.get_rect(
				center=(WIDTH//12 , HEIGHT//8)))
			WIN.blit(plife_text, plife_text.get_rect(
				center=(3*(WIDTH//12) -200, HEIGHT//4)))
			WIN.blit(life_text, life_text.get_rect(
				center=(3*(WIDTH//12), HEIGHT//4)))
										   

		else:
			# self.SwitchToScene(self.main)
			self.result = 0
			pwin_text = self.font.render(pwin_text, True,
										  (0, 0, 0))
			pattempt_text = self.font.render(pattempt_text, True,
										   (0, 0, 0))
			plife_text = self.font.render(plife_text, True,
										   (0, 0, 0))

			WIN.blit(pwin_text, pwin_text.get_rect(
				center=(WIDTH//4, HEIGHT//2)))
			WIN.blit(pattempt_text, pattempt_text.get_rect(
				center=(WIDTH//2 - 60, HEIGHT//2)))
			WIN.blit(plife_text, plife_text.get_rect(
				center=(3*WIDTH//4, HEIGHT//2)))
										   


