from .scene_base import SceneBase
import pygame
from UI_Objects.button import Button
from CONSTANTS import *
from time import sleep
import maze_mini_game as maze


class MazeScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.img = pygame.image.load("maze_mini_game/hugo.png").convert_alpha()
        self.deg = 0
        self.result = None
        self.slide = 0
        self.game = maze.MazeMiniGame()
        self.game.test_maze()
        self.view = maze.MazeView(self.game)
        print("New Maze game")

    def ProcessInput(self, events, pressed_keys, game_params):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("MOUSE CLICK: ", end="")

    def Update(self):
        if self.result is None:
            print("Maze run")
            self.result = self.game.play_game()
        return 0

    def Render(self, WIN):
        # For the sake of brevity, the title scene is a blank red screen
        if self.result is None:
            self.view.draw_background(WIN)
            self.view.draw_board(WIN)                   
        else:
             # self.SwitchToScene(self.main)
            self.result = 0
        
