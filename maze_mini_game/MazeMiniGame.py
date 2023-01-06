from .maze import Maze
from time import perf_counter
from Util import dotimer


furhat_turn_start_texts = ["Where do you wanna go?","I am listening", "your move?","okay whats next"]

numbers = {'1':('1','one','woman','ron','mom','swan','bond','run','volume'), 
'2':('2','two','to','club'),
'3':('3','three','tree','siri'),
'4':('4','four','for','poor','fall'),
'5':('5','five','volume'),
'6':('6','six','SEX'), 
'7':('7','seven','11'), 
'8':('8','eight') }

directions = {'left' : ('left','leaf','leaves','lefts'), 'right' : ('right','rights','write','rides'), 'down' : ('down','dumb','thumb','thong','dong','noun'), 'up' : ('up','lock','of','off')}

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
                response = self.furhat.ask_one_of_them(furhat_turn_start_texts)
                success, num, direction = self.parse_answer(response)
                            
                if success:
                    for _ in range(num):
                        if direction == "left":
                            if not self.maze.moveLeft():
                                self.furhat.say('Thats the farthest point you can go')
                                break
                        elif direction == "right":
                            if not self.maze.moveRight():
                                self.furhat.say('Thats the farthest point you can go')
                                break
                        elif direction == "up":
                            if not self.maze.moveUp():
                                self.furhat.say('Thats the farthest point you can go')
                                break       
                        elif direction == "down":
                            if not self.maze.moveDown():
                                self.furhat.say('Thats the farthest point you can go')
                                break
                else:
                    print("Wrong input")
                    continue
            else:
                print("You have won")
                return 'MAZE',1, None, None

    def end_flow(self):
        print("Sorry times out")
    
    def parse_answer(self,response):
        words = response.split()
        success, num, direction = False, 1, None
        
        for dv, possibilities in directions.items():
            for possibility in possibilities:
                if possibility in words:
                    direction = dv
                    success = True

        if not direction:
            return False, None, None

        for number, possibilities in numbers.items():
            for possibility in possibilities:
                print(possibility)
                if possibility in words:
                    num = number

        return success, int(num), direction
        