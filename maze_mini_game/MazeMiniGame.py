from .maze import Maze
from time import perf_counter
from Util import dotimer


furhat_turn_start_texts = ["Where do you wanna go?","I am listening", "your move?","okay whats next"]

numbers = {'1':('1','one','woman','ron','mom','swan','bond','run','volume'), 
'2':('2','two','to','club'),
'3':('3','three','tree','siri'),
'4':('4','four','for','poor'),
'5':('5' 'five'),
'6':('6','six','SEX'), 
'7':('7','seven','11'), 
'8':('8','eight') }

class MazeMiniGame():
    def __init__(self, maze,time_left,furhat):
        self.maze = maze
        self.time_left = time_left
        self.furhat = furhat

        #self.introduction()
    
    def introduction(self):
        self.furhat.say(f"You are trying to go to the computer tribe. Tell me your moves for each turn, like 5 down. So that you can progress in the maze")

    def play_game(self):       
        dotimer.do_intime(self.play_flow, self.end_flow, self.time_left)

    def play_flow(self):
        while True:
            if not self.maze.isWin: 
                answer = self.furhat.ask_one_of_them(furhat_turn_start_texts)
                
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