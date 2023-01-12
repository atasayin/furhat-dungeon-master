import cv2
from deepface import DeepFace
import time
import warnings
import random

class EmotionMiniGame:
    def __init__(self):
        self.n_emotion = ""
        self.n_percantage = ""
        self.d_emotion = ""
        self.d_emotion_percantege = ""
        self.furhat = None
        self.total_emotion_count = 2
        self.to_exclude = []

    def capture_write(
        self, filename="image.jpeg", port=0, ramp_frames=30, x=1280, y=720
    ):
        camera = cv2.VideoCapture(port)

        # Set Resolution
        camera.set(3, x)
        camera.set(4, y)

        # Adjust camera lighting
        for i in range(ramp_frames):
            temp = camera.read()
        retval, im = camera.read()
        cv2.imwrite(filename, im)
        del camera
        return True

    def check_emotion(self, obj, emotion_list, attempt,number):
        emotion = emotion_list[number]
        result = False
        print("EMOTION IS: ", emotion[1])
        # define percantage range to be considered as matching print emotion statmnet should be changed look at keyboard waiting things
        emotion_status = int(obj.get("emotion").get(emotion[1]))
        print("EMOTION STATUS IS ", emotion_status)
        result = obj.get("emotion")
        max = 0.1
        d_emotion = None
        for emotion, value in obj.get("emotion").items():
            if value > max:
                max = value
                d_emotion = emotion
        print("result STATUS IS ", result)
        print("max STATUS IS ", max)
        print("d_emotion STATUS IS ", d_emotion)
        print("emotion[2] is", emotion[2])
        print("emotion[1] is", emotion[1])
        print("emotion_status is", emotion_status)
        if 20 + int(self.n_percantage) >= emotion_status >= int(self.n_percantage) - 20:
            print(f" YOU MATCHED {emotion_list[number][1]} WITH {emotion_status} percent")
            self.furhat.say(
                f" YOU MATCHED {emotion_list[number][1]} WITH {emotion_status} percent"
            )
            result = True
            self.d_emotion = d_emotion
            self.d_emotion_percantege = str(float("{:.2f}".format(max)))
        else:
            print(f" YOU DID NOT MATCHED YOUR EMOTIONS WERE : {obj}")
            self.furhat.say(
                f" YOU DID NOT MATCHED YOUR EMOTIONS , YOUR MOST DOMINANT EMOTION WAS : {d_emotion}"
            )
            attempt = attempt + 1
            self.d_emotion = d_emotion
            self.d_emotion_percantege = str(float("{:.2f}".format(max)))
            result = False

        return attempt, result

    def play_game(self):
        warnings.filterwarnings("ignore")

        emotion_list = (
            (("Happy 80%"), "happy", 80),
            (("Sad 80%"), "sad", 80),
            (("Angry 70%"), "angry", 70),
            (("Happy 10%"), "happy", 10),
            (("Fear 80%"), "fear", 80),
            (("Neutral 80%"), "neutral", 80),
            (("Disgust 70%"), "disgust", 70),
            (("Surprise 70%"), "surprise", 70)
        )
        win_count = 0
        for i in range(1, 2):
            print(f"NOW YOU ARE IN TURN {i} ")
            self.furhat.say(
                f"NOW YOU ARE IN TURN {i} AND YOUR Total Attempt count is 3 "
            )
            result = False
            attempt = 0
            number = random.randint(0, len(emotion_list))
            for line in open('emotion_mini_game/AskedQuestions.txt', "r").readlines():
                self.to_exclude.append(int(line))
                print("LEN EMOTION LIST ",len(emotion_list) )
            while number in self.to_exclude:
                number = random.randint(0, len(emotion_list)-1)
            self.to_exclude.append(number)
            print("TO EXCLUDE ", self.to_exclude)
            emotion = emotion_list[number]
            self.n_emotion = emotion[1]
            self.n_percantage = emotion[1 + 1]
            print("self.n_percantage ", self.n_percantage)
            while attempt < 2:
                if not result:
                    print("Attempt for this turn is ", attempt+1)
                    self.furhat.say(f"Attempt for this turn is {attempt+1} ")
                    print(
                        f"IN TURN {i} YOU NEED TO MATCH {self.n_emotion} {self.n_percantage} percent "
                    )
                    self.furhat.say(
                        f"IN TURN {i} YOU NEED TO MATCH {self.n_emotion} "
                    )
                    self.furhat.say(f"GET READY You Have 3 Seconds ")

                    if attempt > 1:
                        self.furhat.look_at_other_player()
                        self.furhat.say(f"HMM You seem to need help. Let me show you have I express {self.n_emotion}")
                        self.furhat.say(f"Watch it very carefully")
                        if self.n_emotion == 'happy':
                            self.furhat.get_gesture("BigSmile")
                        elif self.n_emotion == 'Sad' :
                            self.furhat.get_gesture("ExpressSad")
                        elif self.n_emotion == 'Angry':
                            self.furhat.get_gesture("ExpressAnger")
                        elif self.n_emotion == 'disgust':
                            self.furhat.get_gesture("ExpressDisgust")
                        elif self.n_emotion == 'surprise':
                            self.furhat.get_gesture("Surprise")
                        elif self.n_emotion == 'fear':
                            self.furhat.get_gesture("ExpressFear")
                    time.sleep(3)
                    capture = self.capture_write()
                    if capture:
                        turn = i
                        turn = turn - 1
                        try:
                            obj = DeepFace.analyze(
                                img_path="image.jpeg", actions=["emotion"]
                            )
                            attempt, result = self.check_emotion(
                                obj, emotion_list, attempt,number
                            )
                            time.sleep(5)
                        except:
                            print("YOUR FACE CANNOT BE FOUND")
                            self.furhat.say(
                                text=f"DO NOT HIDE YOUR FACE ", blocking=True
                            )
                            attempt = attempt + 1
                            result = False

                else:
                    win_count = win_count + 1
                    break
        for num in self.to_exclude:
            file = open("emotion_mini_game/AskedQuestions.txt",
                        "a")  # Opens a file for writing and puts it in the file variable
            file.write(f"{num}\n")  # Writes the entire list + the appended element into new file
            file.close()  # Closes the file

        return win_count