
from os import getcwd
from pathlib import Path
import random
from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from PIL import Image as PImage

class ChessMiniGame():
    def __init__(self):
        self.is_win = 0
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
            life = 2
            to_exculude = []
            while life > 0 and win < 3:
                attempt = 2
                print("REMANING Life : ",life, "Total Win : ", win)
                number =random.randint(1,20)
                print("TO EXCULUDE : ", to_exculude)
                while number in to_exculude :
                    number =random.randint(1,20)
                print(number)

                key = solution[number]
                print(key)
                
                to_exculude.append(number)
                img = PImage.open(path + '/'+str(number)+'.png')
                img.show() 
                
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
                
                while attempt >0:
                    response = furhat.listen()
                    sleep(3)
                    print(response)
                    furhat.listen_stop()
                    piece,cord,row,result = self.is_Valid(response)
                    print("PIECE AND RESULT IS ",piece,cord,row,result)
                    if result:
                        print("GOT IT")
                        tried = piece+''+cord+''+row
                        break
                    attempt = attempt -1
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
                else :
                    furhat.say(text="NOOO, that was wrong",blocking=True)
                    print("NOOO")
                    print(tried,answer)
                    life -=1
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
        chess_piece = {'Q': ('QUEEN','Queen','Green','green','GREEN','queen'),'R': ('ROOK','Cook','COOK','rook','Rook'),'N': ('KNIGHT','LIKE','Knigth','knigth' ,'NIGTH','igth','IGTH','nigth'),
            'B': ('BISHOP','ISHOP','ishop','Bishop','bishop'),'K' : 'KING','P':'PAWN'}
        coordinate = {'A':('A'), 'B':('B','BE'),'C':('C','SEE','SEA'),'D':('D'),'E':('E'), 'F':('F','EF'), 'G':('G','J','JEE'), 'H':('H','8','AGE') }
        row = {'1':('1'), '2':('2'),'3':('3'),'4':('4'),
        '5':('5'),'6':('6','SEX'), '7':('7'), '8':('8') }
        for piece, value in chess_piece.items():
            for val in value:
                if val in response.message:
                    check = True
                    m_piece = piece                  
                    
        if check:
            print("first check")
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
