from os import getcwd
from pathlib import Path
from pickle import NONE
import random
from time import sleep
from PIL import Image as PImage
import pygame
from CONSTANTS import *
from furhat_remote_api import FurhatRemoteAPI



class QuizMiniGame():
    def __init__(self):
        self.intro = True
        self.solution = {1: "C", 2: "B", 3: "C", 4: "A", 5: "B", 6: "D", 7: 'B'}
        self.answers = {
            "A": ("A", "18","1992",'42','BROWN','Mars','1983'),
            "B": ("B", "BEE", "BE", "20","1993",'33','RED','Jupiter','1989'),
            "C": ("C", "SEE", "SAY", "SEA", "22","1994",'27','YELLOW','Venus','WHITE','1979'),
            "D": ("D", "DC", "24","1995",'25','GREEN','Mercury','1982'),
        }
        self.questions = {
            1: "How many undergraduate programs there are at Koç University?",
            2: "Which year Koç University was founded?",
            3: "What is the ratio between double major graduates and non-double major graduates in 2019?",
            4: "What is the rarest M&M color?",
            5: "Which planet is the hottest in the solar system?",
            6: "What color is Absinthe?",
            7: "When did the Cold War end?"
        }
        self.choices = {
            1: ("A is 18", "B is 20", "C is 22", "D is 24"),
            2: ("A is 1992", "B is 1993", "C is 1994", "D is 1995"),
            3: ("A is 42", "B is 33", "C is 27", "D is 25"),
            4: ("A is BROWN", "B is RED", "C is YELLOW", "D is GREEN"),
            5: ("A is Mars", "B is Jupiter", "C is Venus", "D is Mercury"),
            6: ("A is BROWN", "B is RED", "C is WHITE", "D is GREEN"),
            7: ("A is 1983", "B is 1989", "C is 1979", "D is 1982")

        }
        self.button_choices = {
            1: {"A": 18, "B": 20, "C": 22, "D": 24},
            2: {"A": 1992, "B": 1993, "C": 1994, "D": 1995},
            3: {"A": 42, "B": 33, "C": 27, "D": 25},
            4: {"A": 'BROWN', "B": 'RED', "C": 'YELLOW', "D": 'GREEN'},
            5: {"A": 'Mars', "B":'Jupiter', "C": 'Venus', "D": 'Mercury'},
            6: {"A": 'BROWN', "B": 'RED', "C": 'WHITE', "D": 'GREEN'},
            7: {"A": '1983', "B": '1989', "C": '1979', "D": '1982'},

        }
        self.furhat = FurhatRemoteAPI("localhost")
        self.win_count = 0
        self.question_number = 0
        self.question_count = 0
        self.attempt_count = 3
        self.correct = True
        self.path = "quiz_mini_game/millionaire.jpeg"
        self.user_choice = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.is_true = None
        self.to_exclude = []


    def is_valid(self, response):
        message = response.message
        message = message.upper()
        print(message)
        answer = None
        result = False
        flag = False
        for choice, value in self.answers.items():
            if flag != True:
                for val in value:
                    if flag != True:
                        if val in message:
                            answer = choice
                            result = True
                            flag =  True
                            break
        return answer, result

    def is_correct(self, answer):
        key = self.solution.get(self.question_number)
        if key == answer:
            self.is_true = True
            sleep(1)
            self.furhat.say(text=f"{key} is correct!", blocking=True)
            print("YASS")
            self.win_count = self.win_count + 1
        else:
            self.is_true = False
            self.furhat.say(
                text=f"NOOO, {answer} is the wrong choice the correct one was {key}",
                blocking=True,
            )
            print("NOOO")
            self.correct = False

    def play_game(self):
        sleep(3)
        self.intro = False
        path = "quiz_mini_game/Questions"
        for line in open('quiz_mini_game/AskedQuestions.txt', "r").readlines():
            self.to_exclude.append(int(line))
        print( "Exclude", self.to_exclude)  # Prints out the
        while self.question_count <= 0:
            print("Total Win : ", self.win_count)
            number = random.randint(1, 7)
            print("THE QUESTION NUMBER IS : ", number)
            while number in self.to_exclude:
                number = random.randint(1, 7)
            self.question_number = number
            self.to_exclude.append(number)
            # img = PImage.open(path + '/'+str(number)+'.png')
            self.path = path + "/" + str(number) + ".png"
            # self.SceneBase.img = pygame.image.load(path + '/'+str(number)+'.png').convert_alpha()
            # self.SceneBase.img = pygame.transform.scale(self.SceneBase.img, (WIDTH, HEIGHT))
            self.A = self.button_choices.get(number).get("A")
            self.B = self.button_choices.get(number).get("B")
            self.C = self.button_choices.get(number).get("C")
            self.D = self.button_choices.get(number).get("D")

            self.question_count = self.question_count + 1
            self.furhat.say(text=f"Question {self.question_count} is", blocking=True)
            self.furhat.say(text=self.questions.get(number), blocking=True)
            self.furhat.say(text=f"THE CHOICES ARE {self.choices.get(number)}")
            self.furhat.say(text="YOU HAVE 10 SECONDS TO ANSWER", blocking=True)

            sleep(5)
            while self.attempt_count > 0:
                self.furhat.say(text="AND YOUR ANSWER IS?", blocking=True)
                response = self.furhat.listen()
                print(response)
                self.furhat.listen_stop()
                try:
                    answer, result = self.is_valid(response)
                    if result:
                        self.furhat.say(
                            text=f"Your Answer is {answer} {self.button_choices.get(number).get(answer)} ",
                            blocking=True,
                        )
                        self.furhat.say(text="ARE YOU SURE??", blocking=True)
                        response = self.furhat.listen()
                        message = response.message
                        message = message.upper()
                        print("SURE RESPONSE ", message)
                        if message in ("YES", "YEAP", '"YEAH'):
                            self.user_choice = answer
                            print("user_choice", self.user_choice)
                            sleep(3)
                            print("GOT IT")
                            break
                    else:
                        self.attempt_count = self.attempt_count - 1
                        self.furhat.say(
                            text="I couldn't understand your response", blocking=True
                        )
                        sleep(1)
                except:
                    answer, result = None, False
                print("Answer AND RESULT IS ", answer, result)

            sleep(2)
            self.is_correct(answer)
            for num in self.to_exclude:
                file = open("quiz_mini_game/AskedQuestions.txt", "a")  # Opens a file for writing and puts it in the file variable
                file.write(f"{num}\n")  # Writes the entire list + the appended element into new file
                file.close()  # Closes the file

        if self.correct and self.win_count >= 1:
            self.furhat.say(text="YOU WON THE GAME")
            self.result = 1
        else:
            self.result = 0
        return self.win_count
