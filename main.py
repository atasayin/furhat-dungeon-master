import pygame
from CONSTANTS import *
import math
from UI_Objects.button import Button

from furhat_remote_api import FurhatRemoteAPI
from time import sleep
import time

furhat_last_spoke = time.time()

furhat = FurhatRemoteAPI("localhost")

# furhat.say(text="Imam hatipler kapatilsin", blocking=True)
# furhat.say(text="Kafana sikacagim gunu bekle hahaha", blocking=True)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Master")
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)


FPS = 120
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()

furhat_img = pygame.image.load("furhat.jpeg").convert_alpha()



run = True
deg = 0

game_state = "intro"
slide = 0

while run:

	if game_state is "intro":
		WIN.fill(WHITE)
		mousepos = pygame.mouse.get_pos()
		clock.tick(FPS)
		PLAY_BUTTON = Button(image=pygame.image.load("play_button.jpeg").convert_alpha(), pos=(WIDTH/2 + math.cos(deg/2) * 20, HEIGHT-200), text_input=None, font=font, base_color=(240, 0, 0), hovering_color=BLACK, scale=0.35)

		PLAY_BUTTON.changeColor(mousepos)
		PLAY_BUTTON.update(WIN)


		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAY_BUTTON.checkForInput(mousepos):
					print("BASIS")
					game_state = "fur"
		deg += 0.03

		text = font.render("Furhat", True, BLACK)
		text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2  + math.sin(deg) * 40 - 50))
		WIN.blit(text, text_rect)
		pygame.display.update()
		

	elif game_state is "fur":
		WIN.fill(WHITE)
		WIN.blit(furhat_img, (0-slide,0))
		slide += 0.1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	if time.time() - furhat_last_spoke > 5:
		furhat_last_spoke = time.time()
		furhat.say(text="n")

# pygame.quit()
