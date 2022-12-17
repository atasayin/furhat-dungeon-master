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
            # sleep(1.5)
            # self.result = 0
        return 0

    def Render(self, WIN):
        # For the sake of brevity, the title scene is a blank red screen
        # print(self.result)
        if self.result is None:
            maze = self.game.maze
            WIN.fill((255, 255, 255))
            WIN.blit(self.img, (0-self.slide, 0))

            for y in range(maze.Row):
                for x in range(maze.Col):
                    if maze.grid[x][y] == 1:
                        pygame.draw.rect(WIN, (255, 0, 0),
                                     pygame.Rect(30 * y, 30 * x, 60, 60))
                    
                    elif maze.grid[x][y] == 0:
                        pygame.draw.rect(WIN, (0, 255, 0),
                                         pygame.Rect(30 * y, 30 * x, 60, 60))
                      
                    elif maze.grid[x][y] == 2:
                        pygame.draw.rect(WIN, (0, 0, 255),
                                         pygame.Rect(30 * y, 30 * x, 60, 60))

                    elif maze.grid[x][y] == 3:
                        pygame.draw.rect(WIN, (255, 255, 255),
                                         pygame.Rect(30 * y, 30 * x, 60, 60))                         
                
            self.slide += 0.1
        else:
             # self.SwitchToScene(self.main)
            self.result = 0
        
