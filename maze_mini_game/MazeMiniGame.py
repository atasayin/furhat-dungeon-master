from .maze import Maze
from time import perf_counter
import signal
from Util import dotimer

class MazeMiniGame():
    def __init__(self, maze):
        self.maze = maze
        
    def __init__(self):
        pass
    def test_maze(self):
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
        self.maze = Maze(grid,start_point,end_point)
        self.time_left = 10 #60 * 2
    
    def play_game(self):       
        dotimer.do_intime(self.play_flow,self.end_flow,self.time_left)

    def play_flow(self):
        while True:
            if not self.maze.isWin:            
                answer = input("Where do you wanna go? (left,right, up, down)\n")                
                if answer == "left":
                    self.maze.moveLeft()
                elif answer == "right":
                    self.maze.moveRight()
                elif answer == "up":
                    self.maze.moveUp()
                elif answer == "down":
                    self.maze.moveDown()
                elif answer == "q":
                    return 0
                else:
                    print("Wrong input")
                    continue
            else:
                print("You have won")
                return 1
    def end_flow(self):
        print("Sorry times out")