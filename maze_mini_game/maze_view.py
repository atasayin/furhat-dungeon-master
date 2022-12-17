import pygame
from .location_types import *
import CONSTANTS

class MazeView():
    def __init__(self,mazeGame):
        self.img = pygame.image.load("maze_mini_game/hugo.png").convert_alpha()
        self.game = mazeGame
        self.time_left = mazeGame.time_left
        self.slide = 0
        self.font = CONSTANTS.font
    
    def draw_background(self,WIN):
        WIN.fill((255, 255, 255))
        WIN.blit(self.img, (0-self.slide, 0))
        self.slide += 0.1

    def draw_board(self,WIN):
        mazeLayout = self.game.maze

        for y in range(mazeLayout.Row):
            for x in range(mazeLayout.Col):
                if mazeLayout.grid[x][y] == LocationTypes.WallType:
                    pygame.draw.rect(WIN, (255, 0, 0),
                                    pygame.Rect(30 * y, 30 * x, 60, 60))
                
                elif mazeLayout.grid[x][y] == LocationTypes.RoadType:
                    pygame.draw.rect(WIN, (0, 255, 0),
                                        pygame.Rect(30 * y, 30 * x, 60, 60))
                    
                elif mazeLayout.grid[x][y] == LocationTypes.EndPointType:
                    pygame.draw.rect(WIN, (0, 0, 255),
                                        pygame.Rect(30 * y, 30 * x, 60, 60))

                elif mazeLayout.grid[x][y] == LocationTypes.PlayerType:
                    pygame.draw.rect(WIN, (255, 255, 255),
                                        pygame.Rect(30 * y, 30 * x, 60, 60))
    
    def draw_timeleft(self,WIN):
        self.time_left -= 1.1 * 1/60 
        text = self.font.render(f"{round(self.time_left)}", True, (0, 0, 0))
        WIN.blit(text, text.get_rect(center=(400, 400)))


