import cv2
# from deepface import DeepFace
import time
import warnings


class EmotionMiniGame():
    def __init__(self):
        pass

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
        print(emotion_status,"emotion_status")
        if 20+ int(emotion[2]) >= emotion_status >= int(emotion[2])-20:
                    print(f" YOU MATCHED {emotion[1]} WITH {emotion[1+1]} percent")
                    result = True
        else:
                    print(f" YOU DID NOT MATCHED YOUR EMOTIONS WERE : {obj}")
                    attempt = attempt - 1
                    result = False
                    
        return attempt,result

    def play_game(self):
        warnings.filterwarnings("ignore")
        emotion_list= ((('Happy 80%'),'happy',80),(('Sad 80%'),'sad',80), (('Angry 70%'),'angry',70))
        win_count = 0
        for i in range(1,4):
            print(f"NOW YOU ARE IN TURN {i} ")
            result =False
            attempt = 3
            while attempt >0:
                if not result:
                    print("Attempt for this turn is ", attempt)
                    print(f"IN TURN {i} YOU NEED TO MATCH {emotion_list[i-1][0]} percentages ")
                    time.sleep(3)
                    capture = self.capture_write()
                    if capture:
                        # obj = DeepFace.analyze(img_path = "image.jpeg", 
                        #     actions = ['emotion'])
                        # attempt,result = self.check_emotion(obj,emotion_list,i,attempt)
                        time.sleep(3)
                else:
                    win_count = win_count +1
                    break
        return win_count
