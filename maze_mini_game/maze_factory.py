from .MazeMiniGame import MazeMiniGame
from .maze import Maze 
from .maze_view import MazeView
from .terrain_colors import TerrainColors
from COLORS import *

def MazeFactory(type, furhat):
    if type == "computer":
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
        view = MazeView(game,colors,"maze_mini_game/tribes/comp-tribe.png")

    elif type == "mava":
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
        colors = TerrainColors((253, 1, 0),(247, 105, 21),(238, 222, 4),(160, 214, 54), (47, 162, 54),(51, 62, 212))
        view = MazeView(game,colors,"maze_mini_game/tribes/mava-tribe.png")

    elif type == "mech":
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
        colors = TerrainColors((58,58,58),(131,131,131),(174,174,174),(201,201,201), (229,229,229),(255, 255, 255))
        view = MazeView(game,colors,"maze_mini_game/tribes/mech-tribe.png")

    elif type == "elec":
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
        colors = TerrainColors((0, 100, 200),(128, 128, 0),(255, 200, 0),(255, 0, 0), (0, 0, 0),(148, 0, 211))
        view = MazeView(game,colors,"maze_mini_game/tribes/elec-tribe.png")

    elif type == "medicine":
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
        colors = TerrainColors((0, 100, 200),(128, 128, 0),(255, 200, 0),(255, 0, 0), (0, 0, 0),(148, 0, 211))
        view = MazeView(game,colors,"maze_mini_game/tribes/elec-tribe.png")

    return game, view