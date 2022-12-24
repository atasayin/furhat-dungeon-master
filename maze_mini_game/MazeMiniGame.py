from .maze import Maze
from time import perf_counter
from Util import dotimer

class MazeMiniGame():
    def __init__(self, maze,time_left):
        self.maze = maze
        self.time_left = time_left
        self.furhat = None
    
    def play_game(self):       
        dotimer.do_intime(self.play_flow, self.end_flow, self.time_left)

    def play_flow(self):
        while True:
            if not self.maze.isWin: 
                answer = self.furhat.listen("Where do you wanna go? (left,right, up, down)\n")
                            
                #answer = input("Where do you wanna go? (left,right, up, down)\n")                
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