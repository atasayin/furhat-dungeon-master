# import emotion_mini_game as emotion 
from .scene_base import SceneBase
import pygame
from CONSTANTS import *
# from time import sleep


class EmotionScene(SceneBase):
	def __init__(self,furhat):
		SceneBase.__init__(self)
		self.img = pygame.image.load("emotion_mini_game/balck_gate.jpg").convert_alpha()
		self.img = pygame.transform.scale(self.img, (WIDTH, HEIGHT))
# 		self.deg = 0
# 		self.result = None
# 		self.slide = 0
# 		self.game = emotion.EmotionMiniGame()	
# 		self.game.furhat = furhat
# 		self.font = pygame.font.Font('freesansbold.ttf', 80)	
# 		print("New Emotion game")
	
# 	def ProcessInput(self, events, pressed_keys, game_params):
# 		mousepos = pygame.mouse.get_pos()
# 		for event in events:
# 			if event.type == pygame.MOUSEBUTTONDOWN:
# 				print("MOUSE CLICK: ", end="")
	
# 	def Update(self):
# 		if self.result is None:
# 			print("Emotion GAME STARTED")
# 			self.result = self.game.play_game()
# 			# sleep(1.5)
# 			#self.result = 0
# 		return 0

# 	def Render(self, WIN):
# 		# For the sake of brevity, the title scene is a blank red screen

# 		if self.result is None:
# 			WIN.fill((255, 255, 255))
# 			WIN.blit(self.img, (0, 0))

# 			pn_emotion_text = f"{self.game.n_emotion}"
# 			pd_emotion_text = f"{self.game.d_emotion}"
				
# 			pn_emotion_score_text = f"{self.game.n_percantage}"
# 			pd_emotion_score_text = f"{self.game.d_emotion_percantege}"
# 			pn_emotion_text = self.font.render(pn_emotion_text, True,
# 										  (255,255,255))
# 			pd_emotion_text = self.font.render(pd_emotion_text, True,
# 										   (255,255,255))
# 			pn_emotion_score_text = self.font.render(pn_emotion_score_text, True,
# 										   (255,255,255))
# 			pd_emotion_score_text = self.font.render(pd_emotion_score_text, True,
# 										   (255,255,255))
			

# 			WIN.blit(pn_emotion_text, pn_emotion_text.get_rect(
# 				center=(WIDTH//4+22, HEIGHT//3)))
# 			WIN.blit(pd_emotion_text, pd_emotion_text.get_rect(
# 				center=(WIDTH//4 +480, HEIGHT//3)))
# 			WIN.blit(pd_emotion_score_text, pd_emotion_score_text.get_rect(
# 				center=(WIDTH//4+480, HEIGHT//2)))
# 			WIN.blit(pn_emotion_score_text, pn_emotion_score_text.get_rect(
# 				center=(WIDTH//4+22, HEIGHT//2)))
# 		else:
# 			WIN.fill((255, 255, 255))
# 			WIN.blit(self.img, (0, 0))

# 			pn_emotion_text = f"{self.game.n_emotion}"
# 			pd_emotion_text = f"{self.game.d_emotion}"
# 			pn_emotion_score_text = f"{self.game.n_percantage}"
# 			pd_emotion_score_text = f"{self.game.d_emotion_percantege}"
# 			pn_emotion_text = self.font.render(pn_emotion_text, True,
# 										  (0, 0, 0))
# 			pd_emotion_text = self.font.render(pd_emotion_text, True,
# 										   (0, 0, 0))
# 			pn_emotion_score_text = self.font.render(pn_emotion_score_text, True,
# 										   (0, 0, 0))
# 			pd_emotion_score_text = self.font.render(pd_emotion_score_text, True,
# 										   (0, 0, 0))
			
# 			WIN.blit(pn_emotion_text, pn_emotion_text.get_rect(
# 				center=(WIDTH//4, HEIGHT//2)))
# 			WIN.blit(pd_emotion_text, pd_emotion_text.get_rect(
# 				center=(WIDTH//4-20, HEIGHT//2)))
