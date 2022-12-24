import cv2
from deepface import DeepFace
import time
import warnings


class EmotionMiniGame():
    def __init__(self):
        self.n_emotion = ""
        self.n_percantage = ""
        self.d_emotion = ""
        self.d_emotion_percantege = ""
        self.furhat = None

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

    def check_emotion(self,obj,emotion_list,turn,attempt):
        turn = turn-1
        emotion = emotion_list[turn]
        result = False
        print("EMOTION IS: ",emotion)
        #define percantage range to be considered as matching print emotion statmnet should be changed look at keyboard waiting things
        emotion_status = int(obj.get('emotion').get(emotion[1]))
        print("EMOTION STATUS IS ",emotion_status)
        result = obj.get('emotion')
        max= 0.1
        d_emotion = None
        for emotion, value in obj.get('emotion').items():
            if value > max:
              max = value
              d_emotion = emotion
        print("result STATUS IS ",result)
        print("max STATUS IS ",max)
        print("d_emotion STATUS IS ",d_emotion)
        print("emotion[2] is",emotion[2])
        print("emotion[1] is",emotion[1])
        print("emotion_status is",emotion_status)
        if 20+ int(self.n_percantage) >= emotion_status >= int(self.n_percantage)-20:
                    print(f" YOU MATCHED {emotion[1]} WITH {int(emotion[1+1])} percent")
                    self.furhat.say(f" YOU MATCHED {emotion[1]} WITH {int(emotion[1+1])} percent")
                    result = True
                    self.d_emotion = d_emotion
                    self.d_emotion_percantege = str(float("{:.2f}".format(max)))
        else:
                    print(f" YOU DID NOT MATCHED YOUR EMOTIONS WERE : {obj}")
                    self.furhat.say(f" YOU DID NOT MATCHED YOUR EMOTIONS , YOUR MOST DOMINANT EMOTION WAS : {d_emotion}")
                    attempt = attempt + 1
                    self.d_emotion = d_emotion
                    self.d_emotion_percantege = str(float("{:.2f}".format(max)))
                    result = False
                    
        return attempt,result

    def play_game(self):
        warnings.filterwarnings("ignore")
        
        emotion_list= ((('Happy 80%'),'happy',80),(('Sad 80%'),'sad',80), (('Angry 70%'),'angry',70))
        win_count = 0
        for i in range(1,4):
            print(f"NOW YOU ARE IN TURN {i} ")
            self.furhat.say(f"NOW YOU ARE IN TURN {i} AND YOUR Total Attempt count is 3 ")
            result =False
            attempt = 0
            while attempt <3:
                if not result:
                    print("Attempt for this turn is ", attempt)
                    self.furhat.say(f"Attempt for this turn is {attempt} ")
                    print(f"IN TURN {i} YOU NEED TO MATCH {emotion_list[i-1][0]} percentages ")
                    self.furhat.say(f"IN TURN {i} YOU NEED TO MATCH {emotion_list[i-1][0]} ")
                    self.furhat.say(f"GET READY You Have 3 Seconds ")
                    time.sleep(3)
                    capture = self.capture_write()
                    if capture:
                        turn = i
                        turn = turn-1
                        emotion = emotion_list[turn]
                        self.n_emotion = emotion[1]
                        self.n_percantage = emotion[1+1]
                        print("self.n_percantage ",self.n_percantage)
                        try:
                            obj = DeepFace.analyze(img_path = "image.jpeg", 
                                actions = ['emotion'])
                            attempt,result = self.check_emotion(obj,emotion_list,i,attempt)
                            time.sleep(5)
                        except:
                            print("YOUR FACE CANNOT BE FOUND")
                            self.furhat.say(text=f"DO NOT HIDE YOUR FACE ",blocking=True)
                            attempt = attempt +1
                            result = False

                else:
                    win_count = win_count +1
                    break
        return win_count

