import pygame
pygame.init()

from CONSTANTS import *
import math
from UI_Objects.button import Button

from furhat_remote_api import FurhatRemoteAPI
from time import sleep
import time
from Scenes.title_screen import TitleScene
from Scenes.furhat_photo_screen import FurhatPhotoScene
import threading

furhat_last_spoke = time.time()

furhat = FurhatRemoteAPI("localhost")

screen = pygame.display.set_mode((WIDTH, HEIGHT))


# furhat.say(text="Imam hatipler kapatilsin", blocking=True)
# furhat.say(text="Kafana sikacagim gunu bekle hahaha", blocking=True)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)


FPS = 120
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()

def render_method(scene, event, fps):
	clock = pygame.time.Clock()
	while True:
		clock.tick(fps)
		scene.Render(screen)
		pygame.display.flip()

		if event.is_set():
			break


def run_game(width, height, fps, starting_scene):

	pygame.display.set_caption("Dungeon Master")
	print("running")

	change_scene_event = threading.Event()

	# clock = pygame.time.Clock()

	active_scene = starting_scene
	render_thread = threading.Thread(target=render_method, args=(active_scene, change_scene_event, 60), daemon=True)
	render_thread.start()

	# render_thread = multiprocessing.Process(target=render_method, args=(active_scene,120))
	# render_thread.start()
	update_result = None
	manual_change = False
	
	while active_scene != None:
		pressed_keys = pygame.key.get_pressed()
		
		# Event filtering 
		filtered_events = []
		for event in pygame.event.get():
			quit_attempt = False
			if event.type == pygame.QUIT:
				quit_attempt = True
			elif event.type == pygame.KEYDOWN:
				alt_pressed = pressed_keys[pygame.K_LALT] or \
							  pressed_keys[pygame.K_RALT]
				if event.key == pygame.K_ESCAPE:
					quit_attempt = True
				elif event.key == pygame.K_F4 and alt_pressed:
					quit_attempt = True
			
			if quit_attempt:
				change_scene_event.set()
				active_scene.Terminate()
			else:
				filtered_events.append(event)
		
		active_scene.ProcessInput(filtered_events, pressed_keys)
		if update_result is None:
			# print(f"UPDATE YERI : {active_scene}")
			sleep(0.05)
			update_result = active_scene.Update()
		# active_scene.SwitchToScene(TitleScene())
		# active_scene.Render(screen)

		if update_result is not None:
			# active_scene.SwitchToScene(FurhatPhotoScene())
			# active_scene = active_scene.next
			active_scene = FurhatPhotoScene()
			manual_change = True

			# active_scene = FurhatPhotoScene()
			print(f" NEXT SCENE when switch to furhat: {active_scene.next}")
			update_result = None
		
		if active_scene != active_scene.next or manual_change:
			manual_change = False
			print(f"SCENE CHANGE from {active_scene} to {active_scene.next}")
			change_scene_event.set()
			render_thread.join()

			change_scene_event = threading.Event()
			render_thread = threading.Thread(target=render_method, args=(active_scene.next, change_scene_event, 60), daemon=True)
			render_thread.start()

		active_scene = active_scene.next
		# pygame.display.flip()
		# clock.tick(fps)



run = True
deg = 0

game_state = "intro"
slide = 0

run_game(WIDTH, HEIGHT, 120, TitleScene())


# 	if game_state is "intro":
# 		WIN.fill(WHITE)
# 		mousepos = pygame.mouse.get_pos()
# 		clock.tick(FPS)
# 		PLAY_BUTTON = Button(image=pygame.image.load("play_button.jpeg").convert_alpha(), pos=(WIDTH/2 + math.cos(deg/2) * 20, HEIGHT-200), text_input=None, font=font, base_color=(240, 0, 0), hovering_color=BLACK, scale=0.35)

# 		PLAY_BUTTON.changeColor(mousepos)
# 		PLAY_BUTTON.update(WIN)


		
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				run = False
# 			if event.type == pygame.MOUSEBUTTONDOWN:
# 				if PLAY_BUTTON.checkForInput(mousepos):
# 					print("BASIS")
# 					game_state = "fur"
# 		deg += 0.03

# 		text = font.render("Furhat", True, BLACK)
# 		text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2  + math.sin(deg) * 40 - 50))
# 		WIN.blit(text, text_rect)
# 		pygame.display.update()
		

# 	elif game_state is "fur":
# 		WIN.fill(WHITE)
# 		WIN.blit(furhat_img, (0-slide,0))
# 		slide += 0.1

# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				run = False

# 		pygame.display.update()

# 	if time.time() - furhat_last_spoke > 5:
# 		furhat_last_spoke = time.time()
# 		furhat.say(text="n")

# pygame.quit()
