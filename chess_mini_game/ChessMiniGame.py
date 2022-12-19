
from os import getcwd
from pathlib import Path
import random
from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from PIL import Image as PImage
import pygame
from CONSTANTS import HEIGHT, WIDTH
from Scenes.scene_base import SceneBase

class ChessMiniGame():
    def __init__(self,Scene):
        self.is_win = 0
        self.SceneBase = Scene
        self.win_count = 0
        self.attempt_count = -1
        self.life_count = 3
        

    def OneMoveChess(self):
            furhat = FurhatRemoteAPI("localhost")
            solution = {1:'WQB7', 2:'WRE5', 3:'BQH5',4:'BQD4',5:'BQA1',6:'WRH4',7:'WQF7',8:'WQH7',9:'WQG7',10:'WNF7',
                        11:'WBG6',12:'BQH2', 13:'WQE5',14:'WBH6',15:'WQC6',16:'WBH7',
                        17:'WNH6',18:'WRD8',19:'WRH4',20:'WNF6'}

            chess_piece = {'Q': 'QUEEN','R': 'ROOK','N': 'KNIGHT',
            'B': 'BISHOP','K' : 'KING','P':'PAWN'}
            print(type(solution))
            path =  "chess_mini_game/ChessOneMove"
            win  = 0
            self.win_count = win
            life = 3
            self.life_count =life
            to_exculude = []
            while life > 0 and win < 3:
                attempt = 2
                self.attempt_count = attempt
                print("REMANING Life : ",life, "Total Win : ", win)
                number =random.randint(1,20)
                print("TO EXCULUDE : ", to_exculude)
                while number in to_exculude :
                    number =random.randint(1,20)
                print(number)

                key = solution[number]
                print(key)
                
                to_exculude.append(number)
                #img = PImage.open(path + '/'+str(number)+'.png')
                self.SceneBase.img = pygame.image.load(path + '/'+str(number)+'.png').convert_alpha()
                self.SceneBase.img = pygame.transform.scale(self.SceneBase.img, (WIDTH, HEIGHT))

                #img.show() 
                
                if 'W' in  key:
                    furhat.say(text="White's move mate in one move",blocking=True)
                    print("White's move mate in one move")
                else:
                    furhat.say(text="Black's move mate in one move",blocking=True)
                    print("Black's move mate in one move")
                
                sleep(2)
                move= key[2:]
                piece = key[1]
                answer = key[1:]
                print(move)
                print('NEEDED MOVE: '+ chess_piece[piece]+' MOVE TO ' +move)
                furhat.say(text="You have 10 seconds to think, when I say I am listening, please say your answer",blocking=True)
                sleep(10)
                while attempt >0:
                    furhat.say(text="I am listening",blocking=True)
                    response = furhat.listen()
                    print(response)
                    furhat.listen_stop()
                    piece,cord,row,result = self.is_Valid(response)
                    print("PIECE AND RESULT IS ",piece,cord,row,result)
                    if result:
                        print("GOT IT")
                        tried = piece+''+cord+''+row
                        break
                    attempt = attempt -1
                    self.attempt_count = attempt
                print(piece)
                if piece in chess_piece.keys():
                    print("I UNDERSTAND")
                else:
                    furhat.say(text="I couldn't understand your response please enter it", blocking=True)
                    tried = 'AB6'

                if tried == answer:
                    furhat.say(text="YASS, that was the needed move", blocking=True)
                    print("YASS")
                    print(tried,answer)
                    win  += 1
                    self.win_count = win
                else :
                    furhat.say(text="NOOO, that was wrong",blocking=True)
                    print("NOOO")
                    print(tried,answer)
                    life -=1
                    self.life_count =life
            if life > 0 and win >= 3:
                    furhat.say(text="YOU WON THE GAME")
                    self.is_win = 1 

    def evaluate_chose(self,choice):
        flag = True
        while flag:
            if choice == 1:
                flag= False
                self.OneMoveChess()
            #elif choice == 2:
            #    flag= False
            #    TwoMoveChess()
            else:
                print("NOT A VALID CHOICE")

    def is_Valid(self,response):
        flag = False
        m_piece = None
        m_coord = None
        m_row = None
        check = False
        check2 = False
        print(response.message)
        message = response.message
        message = message.upper()
        print(message)
        chess_piece = {'Q': ('QUEEN','Queen','Green','green','GREEN','queen'),'R': ('ROOK','RIBBED','Rick','BROOKE','Cook','COOK','GROUP','rook','Rook','GREEK','ROQUEMORE'),'N': ('KNIGHT','KNIGHTS','LIKE','Knigth','knigth' ,'NIGTH','igth','IGTH','nigth'),
            'B': ('BISHOP','ISHOP','ishop','Bishop','bishop')}
        coordinate = {'H':('H','8','AGE'),'C':('C','SEE','SAY','SEA'),'A':('A'), 'B':('B','BEE','BE'),'D':('D','DC'),'E':('E'), 'F':('F','S','EF','X'), 'G':('G','J','JEE'), }
        row = {'1':('1','WOMAN'), '2':('2'),'3':('3'),'4':('4'),'5':('5'),'6':('6','SEX'), '7':('7','11'), '8':('8') }
        for piece, value in chess_piece.items():
            for val in value:
                if val in response.message:
                    check = True
                    m_piece = piece                  
                    
        if check:
            print("first check")
            for piece in chess_piece.get(m_piece):
                if piece in message:
                    message = message.replace(m_piece, '')
            for coord_key, cor_val in coordinate.items():
                for cor_value in cor_val:
                    if cor_value in response.message :
                        check2 = True
                        m_coord = coord_key
            if check2:
                print("second check")
                for row_key, row_val in row.items():
                    for row_value in row_val:
                        if row_value in response.message :
                            flag = True
                            m_row = row_key
                            return m_piece,m_coord,m_row,flag            
            else:
                return None,None,None,flag 
        else:
            return None,None,None,flag 

    def play_game(self):
            self.evaluate_chose(1)
            return self.is_win
