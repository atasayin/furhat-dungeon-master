from .scene_base import SceneBase
# from Scenes.title_screen import TitleScene
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
import math
import rps_mini_game as rps
from time import sleep


class RPSScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.img = pygame.image.load("rps_mini_game/rock.png").convert_alpha()
        self.result = None
        self.font = pygame.font.Font('freesansbold.ttf', 200)
        self.game = rps.RPSMiniGame()

        print("New RPS game")

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("MOUSE CLICK: ", end="")

    def Update(self):
        if self.result is None:
            self.game.play_game()
            # sleep(1.5)
            print("RPS run")
            self.result = 0

        return 0

    def Render(self, WIN):
        if self.result is None:
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
                center=(WIDTH//4, HEIGHT//2)))
            WIN.blit(vs_text, pleft_text.get_rect(
                center=(WIDTH//2 - 60, HEIGHT//2)))
            WIN.blit(pright_text, pright_text.get_rect(
                center=(3*WIDTH//4, HEIGHT//2)))
