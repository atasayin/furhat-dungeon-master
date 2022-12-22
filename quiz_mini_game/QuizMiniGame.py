
from os import getcwd
from pathlib import Path
from pickle import NONE
import random
from time import sleep
from PIL import Image as PImage
import pygame
from CONSTANTS import HEIGHT, WIDTH
from furhat_remote_api import FurhatRemoteAPI


class QuizMiniGame():
    def __init__(self):
        self.intro = True
        self.solution = {1:'C',2:'B',3:'C',4:'C',5:'C'}
        self.answers = {'A':('A'),'B':('B','BEE','BE'),'C':('C','SEE','SAY','SEA'),'D':('D','DC')}
        self.questions = {1:'How many undergraduate programs there are at Koç University?',
        2:'Which year Koç University was founded?',
        3:'How many undergraduate programs there are at Koç University?',
        4:'How many undergraduate programs there are at Koç University?',
        5:'How many undergraduate programs there are at Koç University?'}
        self.choices = {1:('A is 18','B is 20','C is 22','D is 24'),
        2:('A is 1992','B is 1993','C is 1994','D is 1995'),
        3:('A is 22','B is 20','C is 212','D is 46'),
        4:('A is 22','B is 20','C is 21','D is 46'),
        5:('A is 22','B is 20','C is 21','D is 45')}
        self.furhat = FurhatRemoteAPI("localhost")
        self.win_count  = 0
        self.question_number = 0
        self.question_count=0
        self.attempt_count = 3
        self.correct = True
        self.path = 'quiz_mini_game/millionaire.jpeg'

    def is_valid(self,response):
        message = response.message
        message = message.upper()
        print(message)
        answer = None
        result = False
        for choice, value in self.answers.items():
            for val in value:
                if val in message:
                    answer= choice
                    result = True
        return answer,result

    def is_correct(self,answer):
        key = self.solution.get(self.question_number)
        if key == answer:
            self.furhat.say(text=f"{key} is correct!", blocking=True)
            print("YASS")
            self.win_count = self.win_count +1
        else:
            self.furhat.say(text=f"NOOO, {answer} is the wrong choice the correct one was {key}",blocking=True)
            print("NOOO")
            self.correct =False

    def play_game(self):
        sleep(3)
        self.intro = False
        path =  "quiz_mini_game/Questions"
        
        to_exculude = []
        while self.win_count < 1 and self.correct:
            print("Total Win : ", self.win_count)
            number =random.randint(1,5)
            print("THE QUESTION NUMBER IS : ", number)
            while number in to_exculude :
                number =random.randint(1,5)
            self.question_number = number
            
            to_exculude.append(number)
            #img = PImage.open(path + '/'+str(number)+'.png')
            self.path = path + '/'+str(number)+'.png'
            #self.SceneBase.img = pygame.image.load(path + '/'+str(number)+'.png').convert_alpha()
            #self.SceneBase.img = pygame.transform.scale(self.SceneBase.img, (WIDTH, HEIGHT))
            self.question_count= self.question_count+1
            self.furhat.say(text=f'Question {self.question_count} is',blocking=True)
            self.furhat.say(text=self.questions.get(number),blocking=True)
            self.furhat.say(text=f'THE CHOICES ARE {self.choices.get(number)}') 
            self.furhat.say(text='YOU HAVE 10 SECONDS TO ANSWER',blocking=True)
               
            sleep(5)
            while self.attempt_count >0:
                self.furhat.say(text="AND YOUR ANSWER IS?",blocking=True)
                response = self.furhat.listen()
                print(response)
                self.furhat.listen_stop()
                try:
                    answer,result = self.is_valid(response)
                except:
                     answer,result = None,False 
                print("Answer AND RESULT IS ",answer,result)
                if result:
                    print("GOT IT")
                    break
                else:
                    self.attempt_count =  self.attempt_count - 1
                    self.furhat.say(text="I couldn't understand your response", blocking=True)
            self.is_correct(answer)

           
        if self.correct and self.win_count >= 1:
                self.furhat.say(text="YOU WON THE GAME")
                result =1
        else:
            result = 0
        return result
