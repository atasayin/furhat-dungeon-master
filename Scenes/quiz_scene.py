from .scene_base import SceneBase
# from Scenes.title_screen import TitleScene
import pygame 
#import mixer
from UI_Objects.button import Button
from CONSTANTS import *
import math
import quiz_mini_game as quiz
from time import sleep, time

from furhat_remote_api import FurhatRemoteAPI




class QuizScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.img = pygame.image.load("quiz_mini_game/millionaire.jpeg").convert_alpha()
		self.winner = None
		self.won = False
		self.wontime = 0
		self.result = None
		self.font = pygame.font.Font('freesansbold.ttf', 20)
		self.game = quiz.QuizMiniGame()
		self.furhat = FurhatRemoteAPI("localhost")
		#Load audio file
		# self.mixer = mixer.init()
		# self.mixer.music.load('song.mp3')
		# self.mixer.music.set_volume(0.2)


		print("New QUIZ game")

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
			self.furhat.say(text="Congrats!")
			if self.winner == 1:
				self.furhat.say(text="Right Player wins!", blocking=True)
			else:
				self.furhat.say(text="Left Player wins!", blocking=True)


		# else:
		# 	if time() - self.wontime < 10:
		# 		return None


		return self.result

	def Render(self, WIN):
		path = self.game.path
		self.img = pygame.image.load(path).convert_alpha()
		self.img = pygame.transform.scale(self.img, (WIDTH, HEIGHT))
		if self.result is None:
			# if self.game.intro:
			# 	self.mixer.music.play()
			# 	print("music is resumed....")
			# else:
			# 	self.mixer.music.stop()
			WIN.fill((255, 255, 255))
			WIN.blit(self.img, (0, 0))
			win_text = 'WIN COUNT:'
			pwin_text = f"{self.game.win_count}"
			quest_text = 'Question Number:'
			pquestion_text = f"{self.game.question_count}"
			
			pwin_text = self.font.render(pwin_text, True,
										  (0, 0, 0))
			win_text = self.font.render(win_text, True,
										  (0, 0, 0))
			pquestion_text = self.font.render(pquestion_text, True,
										   (0, 0, 0))
			quest_text = self.font.render(quest_text, True,
										   (0, 0, 0))

			WIN.blit(win_text, win_text.get_rect(
				center=((WIDTH//8), HEIGHT//5)))
			WIN.blit(pwin_text, pwin_text.get_rect(
				center=((WIDTH//8)+100, HEIGHT//5)))
			WIN.blit(pquestion_text, pquestion_text.get_rect(
				center=((WIDTH//8)+100, HEIGHT//4)))
			WIN.blit(quest_text, quest_text.get_rect(
				center=((WIDTH//8), HEIGHT//4)))

		else:
			WIN.fill((255, 255, 255))
			WIN.blit(self.img, (0, 0))

		