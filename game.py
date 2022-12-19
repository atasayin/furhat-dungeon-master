import threading
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


furhat_last_spoke = time.time()


# screen = pygame.display.set_mode((WIDTH, HEIGHT))



FPS = 60
font = pygame.font.SysFont(None, 100)
clock = pygame.time.Clock()

class Game:
    def __init__(self) -> None:
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.furhat = FurhatRemoteAPI("localhost")
        self.hope = 50
        self.discontent = 50
        self.run_game(WIDTH, HEIGHT, FPS, TitleScene())


    def render_method(self, scene, event, fps):
        clock = pygame.time.Clock()
        while True:
            clock.tick(fps)
            scene.Render(self.WIN)
            pygame.display.flip()

            if event.is_set():
                break


    def run_game(self, width, height, fps, starting_scene):

        pygame.display.set_caption("Dungeon Master")
        print("running")
        try:
            self.furhat.say(text="Let's Play a game. N-word", blocking=True)
        except Exception:
            print("FURHAT CANNOT BE FOUND")
        change_scene_event = threading.Event()

        # clock = pygame.time.Clock()

        active_scene = starting_scene
        render_thread = threading.Thread(target=self.render_method, args=(active_scene, change_scene_event, 60), daemon=True)
        render_thread.start()

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
                    pygame.quit()
                else:
                    filtered_events.append(event)
            game_params = (self.discontent, self.hope)
            active_scene.ProcessInput(filtered_events, pressed_keys, game_params)
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
                render_thread = threading.Thread(target=self.render_method, args=(active_scene.next, change_scene_event, 60), daemon=True)
                render_thread.start()

            active_scene = active_scene.next


Game()