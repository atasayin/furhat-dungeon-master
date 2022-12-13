import cv2
from deepface import DeepFace
import time


class EmotionMiniGame():
    def __init__(self):
        self.is_win = 0

    def capture_write(self,filename="image.jpeg", port=0, ramp_frames=30, x=1280, y=720):
            camera = cv2.VideoCapture(port)

            # Set Resolution
            camera.set(3, x)
            camera.set(4, y)

            # Adjust camera lighting
            for i in range(ramp_frames):
                temp = camera.read()
            retval, im = camera.read()
            cv2.imwrite(filename,im)
            del(camera)
            return True

    def check_emotion(self,obj,emotion_list,turn,life):
            turn = turn-1
            emotion = emotion_list[turn]
            print(emotion)
            #define percantage range to be considered as matching print emotion statmnet should be changed look at keyboard waiting things

            if obj.get(emotion[1]) == emotion[2]:
                        print(f" YOU MATCHED {emotion[1]} WITH {emotion[1+1]} percent")
            else:
                        print(f" YOU DID NOT MATCHED YOUR EMOTIONS WERE : {obj}")
                        life = life - 1
                        print(f" YOU LOST A LIFE :( REAMINING LIFE COUNT: {life}")
                        
            return life

    def play_game(self):
            l1= ((('Fear 80% and Sad 10%'),'fear',80,'sad',10), (('Angry 70% Disgust 10%'),'angry',70,'disgut',10),(('Happy 80%'),'happy',80))
            print("hello")
            life_count =3
            for i in range(1,4):
                print(f"NOW YOU ARE IN TURN {i} ")
                print(f"IN TURN {i} YOU NEED TO MATCH {l1[i-1][0]} percentages ")
                print("Press q to continue...")
                time.sleep(5)
                capture = self.capture_write()
                if capture:
                    obj = DeepFace.analyze(img_path = "image.jpeg", 
                        actions = ['age', 'gender', 'race', 'emotion'])
                print(obj.get('emotion'))
                life_count = self.check_emotion(obj,l1,i,life_count)
                print("Press q to continue...")
                time.sleep(5)
            if life_count > 0:
                self.is_win = 1
            return self.is_win
