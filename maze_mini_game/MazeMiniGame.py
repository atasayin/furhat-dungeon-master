from .maze import Maze

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
    
    def play_game(self):
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