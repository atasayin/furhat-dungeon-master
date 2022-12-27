from .scene_base import SceneBase

# from Scenes.title_screen import TitleScene
import pygame

# import mixer
from UI_Objects.button import Button
from CONSTANTS import *
import math
import quiz_mini_game as quiz
from time import sleep, time

from UI_Objects import button
from furhat_remote_api import FurhatRemoteAPI


class QuizScene(SceneBase):
    def __init__(self, furhat):
        SceneBase.__init__(self)
        self.img = pygame.image.load("quiz_mini_game/millionaire.jpeg").convert_alpha()
        self.winner = None
        self.won = False
        self.wontime = 0
        self.result = None
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.game = quiz.QuizMiniGame()
        self.furhat = FurhatRemoteAPI("localhost")
        self.button = button.Button(
            image=None,
            pos=(WIDTH / 4, HEIGHT - 300),
            text_input="",
            font=pygame.font.SysFont(None, 50),
            base_color=(0, 0, 0),
            hovering_color=(255, 255, 0),
            scale=0.35,
        )
        self.button3 = button.Button(
            image=None,
            pos=(WIDTH / 4, HEIGHT - 120),
            text_input="",
            font=pygame.font.SysFont(None, 50),
            base_color=(0, 0, 0),
            hovering_color=(255, 255, 0),
            scale=0.35,
        )
        self.button2 = button.Button(
            image=None,
            pos=(WIDTH / 2 + 200, HEIGHT - 300),
            text_input="",
            font=pygame.font.SysFont(None, 50),
            base_color=(0, 0, 0),
            hovering_color=(255, 255, 0),
            scale=0.35,
        )
        self.button4 = button.Button(
            image=None,
            pos=(WIDTH / 2 + 200, HEIGHT - 120),
            text_input="",
            font=pygame.font.SysFont(None, 50),
            base_color=(0, 0, 0),
            hovering_color=(255, 255, 0),
            scale=0.35,
        )

        self.furhat = furhat
        # Load audio file
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
            self.winner = self.game.play_game()
            # sleep(1.5)
            self.won = True
            self.wontime = time()
            self.result = ("QUIZ", self.winner, None, None)
            # self.furhat.say("Congrats!")

        # else:
        # 	if time() - self.wontime < 10:
        # 		return None

        return self.result

    def Render(self, WIN):
        path = self.game.path
        self.img = pygame.image.load(path).convert_alpha()
        self.img = pygame.transform.scale(self.img, (WIDTH, HEIGHT))
        if self.result is None:
            WIN.fill((255, 255, 255))
            WIN.blit(self.img, (0, 0))
            if self.game.user_choice is None and not self.game.intro:
                win_text = "WIN COUNT:"
                pwin_text = f"{self.game.win_count}"
                pwin_text = self.font.render(pwin_text, True, (255, 255, 255))
                win_text = self.font.render(win_text, True, (255, 255, 255))
                WIN.blit(win_text, win_text.get_rect(center=((WIDTH // 8), HEIGHT // 5)))
                WIN.blit(
                pwin_text, pwin_text.get_rect(center=((WIDTH // 8) + 100, HEIGHT // 5)))
                self.button = button.Button(
                    image=None,
                    pos=(WIDTH / 4 + 5, HEIGHT - 245),
                    text_input=f"{self.game.A}",
                    font=pygame.font.SysFont(None, 50),
                    base_color=(255, 255, 255),
                    hovering_color=(255, 255, 0),
                    scale=0.35,
                )
                self.button3 = button.Button(
                    image=None,
                    pos=(WIDTH / 4 + 5, HEIGHT - 104),
                    text_input=f"{self.game.C}",
                    font=pygame.font.SysFont(None, 50),
                    base_color=(255, 255, 255),
                    hovering_color=(255, 255, 0),
                    scale=0.35,
                )
                self.button2 = button.Button(
                    image=None,
                    pos=(WIDTH / 2 + 228, HEIGHT - 245),
                    text_input=f"{self.game.B}",
                    font=pygame.font.SysFont(None, 50),
                    base_color=(255, 255, 255),
                    hovering_color=(255, 255, 0),
                    scale=0.35,
                )
                self.button4 = button.Button(
                    image=None,
                    pos=(WIDTH / 2 + 228, HEIGHT - 104),
                    text_input=f"{self.game.D}",
                    font=pygame.font.SysFont(None, 50),
                    base_color=(255, 255, 255),
                    hovering_color=(255, 255, 0),
                    scale=0.35,
                )
            else:
                if self.game.user_choice == "A":
                    self.button = button.Button(
                        image=None,
                        pos=(WIDTH / 4 + 5, HEIGHT - 245),
                        text_input=f"{self.game.A}",
                        font=pygame.font.SysFont(None, 50),
                        base_color=(255, 255, 0),
                        hovering_color=(255, 255, 0),
                        scale=0.35,
                    )
                elif self.game.user_choice == "B":
                    self.button2 = button.Button(
                        image=None,
                        pos=(WIDTH / 2 + 228, HEIGHT - 245),
                        text_input=f"{self.game.B}",
                        font=pygame.font.SysFont(None, 50),
                        base_color=(255, 255, 0),
                        hovering_color=(255, 255, 0),
                        scale=0.35,
                    )
                elif self.game.user_choice == "C":
                    self.button3 = button.Button(
                        image=None,
                        pos=(WIDTH / 4 + 5, HEIGHT - 104),
                        text_input=f"{self.game.C}",
                        font=pygame.font.SysFont(None, 50),
                        base_color=(255, 255, 0),
                        hovering_color=(255, 255, 0),
                        scale=0.35,
                    )
                elif self.game.user_choice == "D":
                    self.button4 = button.Button(
                        image=None,
                        pos=(WIDTH / 2 + 228, HEIGHT - 104),
                        text_input=f"{self.game.D}",
                        font=pygame.font.SysFont(None, 50),
                        base_color=(255, 255, 0),
                        hovering_color=(255, 255, 0),
                        scale=0.35,
                    )
                if self.game.is_true is not None:
                    if self.game.is_true:
                        if self.game.user_choice == "A":
                            self.button = button.Button(
                                image=None,
                                pos=(WIDTH / 4 + 5, HEIGHT - 245),
                                text_input=f"{self.game.A}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(34, 139, 34),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "B":
                            self.button2 = button.Button(
                                image=None,
                                pos=(WIDTH / 2 + 228, HEIGHT - 245),
                                text_input=f"{self.game.B}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(34, 139, 34),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "C":
                            self.button3 = button.Button(
                                image=None,
                                pos=(WIDTH / 4 + 5, HEIGHT - 104),
                                text_input=f"{self.game.C}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(34, 139, 34),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "D":
                            self.button4 = button.Button(
                                image=None,
                                pos=(WIDTH / 2 + 228, HEIGHT - 104),
                                text_input=f"{self.game.D}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(34, 139, 34),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                    else:
                        if self.game.user_choice == "A":
                            self.button = button.Button(
                                image=None,
                                pos=(WIDTH / 4 + 5, HEIGHT - 245),
                                text_input=f"{self.game.A}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(255, 0, 0),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "B":
                            self.button2 = button.Button(
                                image=None,
                                pos=(WIDTH / 2 + 228, HEIGHT - 245),
                                text_input=f"{self.game.B}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(255, 0, 0),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "C":
                            self.button3 = button.Button(
                                image=None,
                                pos=(WIDTH / 4 + 5, HEIGHT - 104),
                                text_input=f"{self.game.C}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(255, 0, 0),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                        elif self.game.user_choice == "D":
                            self.button4 = button.Button(
                                image=None,
                                pos=(WIDTH / 2 + 228, HEIGHT - 104),
                                text_input=f"{self.game.D}",
                                font=pygame.font.SysFont(None, 50),
                                base_color=(255, 0, 0),
                                hovering_color=(255, 255, 0),
                                scale=0.35,
                            )
                    self.correct_button()

            self.button.update(WIN)
            self.button2.update(WIN)
            self.button3.update(WIN)
            self.button4.update(WIN)

            # quest_text = "Question Number:"
            # pquestion_text = f"{self.game.question_count}"

           
            # pquestion_text = self.font.render(pquestion_text, True, (0, 0, 0))
            # quest_text = self.font.render(quest_text, True, (0, 0, 0))


            # WIN.blit(
            #     pquestion_text,
            #     pquestion_text.get_rect(center=((WIDTH // 8) + 100, HEIGHT // 4)),
            # )
            # WIN.blit(
            #     quest_text, quest_text.get_rect(center=((WIDTH // 8), HEIGHT // 4))
            # )
        else:
            WIN.fill((255, 255, 255))
            WIN.blit(self.img, (0, 0))

    def correct_button(self):
        correct_button = self.game.solution.get(self.game.question_number)
        if correct_button == "A":
            self.button = button.Button(
                image=None,
                pos=(WIDTH / 4 + 5, HEIGHT - 245),
                text_input=f"{self.game.A}",
                font=pygame.font.SysFont(None, 50),
                base_color=(0, 255, 0),
                hovering_color=(255, 255, 0),
                scale=0.35,
            )
        elif correct_button == "B":
            self.button2 = button.Button(
                image=None,
                pos=(WIDTH / 2 + 228, HEIGHT - 245),
                text_input=f"{self.game.B}",
                font=pygame.font.SysFont(None, 50),
                base_color=(0, 255, 0),
                hovering_color=(255, 255, 0),
                scale=0.35,
            )
        elif correct_button == "C":
            self.button3 = button.Button(
                image=None,
                pos=(WIDTH / 4 + 5, HEIGHT - 104),
                text_input=f"{self.game.C}",
                font=pygame.font.SysFont(None, 50),
                base_color=(0, 255, 0),
                hovering_color=(255, 255, 0),
                scale=0.35,
            )
        elif correct_button == "D":
            self.button2 = button.Button(
                image=None,
                pos=(WIDTH / 2 + 228, HEIGHT - 104),
                text_input=f"{self.game.D}",
                font=pygame.font.SysFont(None, 50),
                base_color=(0, 255, 0),
                hovering_color=(255, 255, 0),
                scale=0.35,
            )
