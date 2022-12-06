from furhat_remote_api import FurhatRemoteAPI
from maze import Maze


def play_game():
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
    end_point = 1, 2 #2,5
    maze = Maze(grid,start_point,end_point)

    while True:
        if not maze.isWin:
            answer = input("Where do you wanna go? (left,right, up, down)\n")

            if answer == "left":
                maze.moveLeft()
            elif answer == "right":
                maze.moveRight()
            elif answer == "up":
                maze.moveUp()
            elif answer == "down":
                maze.moveDown()
            elif answer == "q":
                break
            else:
                print("Wrong input")
                continue
        else:
            print("You have won")
            break




