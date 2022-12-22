import chess_mini_game as chess 
from .scene_base import SceneBase
import pygame
from CONSTANTS import *
from time import sleep


class ChessScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.img = pygame.image.load("chess_mini_game/chess.jpg").convert_alpha()
		self.deg = 0
		self.result = None
		self.slide = 0
		self.font = pygame.font.Font('freesansbold.ttf', 20)
		self.game = chess.ChessMiniGame()	

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
		path = self.game.path
		self.img = pygame.image.load(path).convert_alpha()
		self.img = pygame.transform.scale(self.img, (WIDTH, HEIGHT))
		# print(self.result)
		if self.result is None:
			WIN.fill((255, 255, 255))
			WIN.blit(self.img, (0, 0))
			win_text = 'WIN COUNT:'
			pwin_text = f"{self.game.win_count}"
			life_text = 'Life COUNT:'
			plife_text = f"{self.game.life_count}"
			
			pwin_text = self.font.render(pwin_text, True,
										  (0, 0, 0))
			win_text = self.font.render(win_text, True,
										  (0, 0, 0))
			plife_text = self.font.render(plife_text, True,
										   (0, 0, 0))
			life_text = self.font.render(life_text, True,
										   (0, 0, 0))

			WIN.blit(win_text, win_text.get_rect(
				center=((WIDTH//8), HEIGHT//5)))
			WIN.blit(pwin_text, pwin_text.get_rect(
				center=((WIDTH//8)+100, HEIGHT//5)))
			WIN.blit(plife_text, plife_text.get_rect(
				center=((WIDTH//8)+100, HEIGHT//4)))
			WIN.blit(life_text, life_text.get_rect(
				center=((WIDTH//8), HEIGHT//4)))
										   
		else:
			# self.SwitchToScene(self.main)
			WIN.blit(self.img, (0, 0))
			if self.game.win_count > 2:
				winner_text = self.font.render("YOU WON THE GAME!", True,
										   (0, 0, 0))
			else:
				winner_text = self.font.render("YOU LOST!", True,
										   (0, 0, 0))
			
			WIN.blit(winner_text, winner_text.get_rect(
				center=(WIDTH/2, HEIGHT/2 - 60)))

										   


