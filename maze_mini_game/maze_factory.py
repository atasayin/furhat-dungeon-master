from .MazeMiniGame import MazeMiniGame
from .maze import Maze 
from .maze_view import MazeView
from .terrain_types import TerrainTypes
from .terrain_colors import TerrainColors
from COLORS import *

def MazeFactory(type, furhat):
    if type == TerrainTypes.COMP_MAZE:
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        start_point = 1, 1
        end_point = 2, 5 #1,2
        maze = Maze(grid,start_point,end_point)
        time_left = 60 * 2
        game = MazeMiniGame(maze,time_left,furhat)
        colors = TerrainColors(github_darker_grey,github_dark_grey,github_light_grey,github_purple,github_blue,github_red)
        view = MazeView(game,colors)

    return game, view