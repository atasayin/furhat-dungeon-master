import pygame
from .location_types import *

BOARD_WIDTH_OFFSET = 250
BOARD_HEIGHT_OFFSET = 50
PLAYER_PIXEL_SIZE = 30
PIXEL_SIZE = 50

class MazeView():
    def __init__(self,mazeGame, colors):
        self.img = pygame.image.load("maze_mini_game/tribes/comp-terrain.png").convert_alpha()
        self.game = mazeGame
        self.time_left = mazeGame.time_left
        self.colors = colors
        self.font = pygame.font.SysFont(None, 100)
        self.fontTerrain = pygame.font.SysFont(None, 38)
    
    def draw_background(self,WIN):
        WIN.fill(self.colors.background)
        pygame.draw.rect(WIN, self.colors.wall, pygame.Rect(50, 50, 175, 175))
        WIN.blit(self.img, (62, 62))
        text = self.fontTerrain.render(f"COMP Terrain", True, self.colors.terrain_text)
        WIN.blit(text, text.get_rect(center=(140, 250)))
    
    def draw_board(self,WIN):
        mazeLayout = self.game.maze

        for y in range(mazeLayout.Row):
            for x in range(mazeLayout.Col):
                rect = pygame.Rect(BOARD_WIDTH_OFFSET + PIXEL_SIZE * y, BOARD_HEIGHT_OFFSET + PIXEL_SIZE * x, PIXEL_SIZE, PIXEL_SIZE)

                if mazeLayout.grid[x][y] == LocationTypes.WallType:
                    pygame.draw.rect(WIN, self.colors.wall, rect)
                
                elif mazeLayout.grid[x][y] == LocationTypes.RoadType:
                    pygame.draw.rect(WIN, self.colors.road, rect)

                elif mazeLayout.grid[x][y] == LocationTypes.EndPointType:
                    pygame.draw.rect(WIN, self.colors.end_point, rect) 
                    
                elif mazeLayout.grid[x][y] == LocationTypes.PlayerType:
                    pygame.draw.rect(WIN, self.colors.road, rect)
                    pygame.draw.rect(WIN, self.colors.player, pygame.Rect(10+BOARD_WIDTH_OFFSET + PIXEL_SIZE * y, 10+BOARD_HEIGHT_OFFSET + PIXEL_SIZE * x, PLAYER_PIXEL_SIZE, PLAYER_PIXEL_SIZE))
    
    def draw_timeleft(self,WIN):
        self.time_left -= 1.1 * 1/60 
        text = self.font.render(f"{round(self.time_left)}", True, self.colors.wall)
        WIN.blit(text, text.get_rect(center=(130, 500)))


