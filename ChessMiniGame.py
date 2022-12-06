
from os import listdir, getcwd
from pathlib import Path
import random
from time import sleep
from PIL import Image as PImage
from furhat_remote_api import FurhatRemoteAPI

furhat = FurhatRemoteAPI("localhost")

def evaluate_chose(choice):
    flag = True
    while flag:
        if choice == 1:
            flag= False
            OneMoveChess()
        elif choice == 2:
            flag= False
            TwoMoveChess()
        else:
            print("NOT A VALID CHOICE")

# def loadImages(path):
#     # return array of images
#     path = getcwd() + "/chess/ChessOneMove"
#     print(path)
#     imagesList = listdir(path)
#     print(imagesList)
#     loadedImages = []
#     for image in imagesList:
#         img = PImage.open(path + '/'+image)
#         img.show() 
#         loadedImages.append(img)

#     return loadedImages


def OneMoveChess():
    print("IN HERE")
    solution = {1:'WQB7', 2:'WRE5', 3:'BQH5',4:'BQD4',5:'BQA1',6:'WRH4',7:'WQF7',8:'WQH7',9:'WQG7',10:'WNF7',
                11:'WBG6',12:'BQH2', 13:'WQE5',14:'WBH6',15:'WQC6',16:'WBH7',
                17:'WNH6',18:'WRD8',19:'WRH4',20:'WNF6'}

    chess_piece = {'Q': 'QUEEN','R': 'ROOK','N': 'KNIGHT',
    'B': 'BISHOP','K' : 'KING','P':'PAWN'}
    print(type(solution))
    path = getcwd() + "/chess/ChessOneMove"
    win  = 0
    life = 2
    to_exculude = []
    while life > 0 and win < 5:
        print("REMANING Life : ",life, "Total Win : ", win)
        number =random.randint(1,20)
        print("TO EXCULUDE : ", to_exculude)
        while number in to_exculude :
            number =random.randint(1,20)
        print(number)

        key = solution[number]
        print(key)
        if 'W' in  key:
            furhat.say(text="White's move mate in one move",blocking=True)
            print("White's move mate in one move")
        else:
            furhat.say(text="Black's move mate in one move",blocking=True)
            print("Black's move mate in one move")
        
        sleep(2)
        to_exculude.append(number)
        img = PImage.open(path + '/'+str(number)+'.png')
        img.show() 

        move= key[2:]
        piece = key[1]
        answer = key[1:]
        print(move)
        print('NEEDED MOVE: '+ chess_piece[piece]+' MOVE TO ' +move)
        response = furhat.listen()
        sleep(3)
        print(response)
        furhat.listen_stop()
        tried = input('Your Move : ')
        if tried == answer:
            furhat.say(text="YASS, that was the needed move", blocking=True)
            print("YASS")
            print(tried,answer)
            win  += 1
        else :
            furhat.say(text="NOOO, that was wrong",blocking=True)
            print("NOOO")
            print(tried,answer)
            life -=1

    #path = "/ChessOneMove/1.png"

# your images in an array
    #imgs = loadImages(path)
    #print(imgs)
    #img = PImage.open(imgs[0])
    #img.show()  


def main():
    print("HELLOO")
    evaluate_chose(1)
    furhat.say(text="YOU WON THE GAME")


if __name__ == "__main__":
    main()
