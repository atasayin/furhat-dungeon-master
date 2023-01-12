from furhat_remote_api import FurhatRemoteAPI
from time import sleep
import json
import os

# furhat = FurhatRemoteAPI("172.23.120.144")
furhat = FurhatRemoteAPI("localhost")

cwd = os.getcwd()
img_folder = os.path.join(cwd, "images")
riff = os.path.join(img_folder, "riff.wav")
print(riff)
furhat.say(text="bruh", blocking=True)
furhat.say(url="/Users/deniz/Desktop/Furh/furhat-dungeon-master/images/riff.wav", lipsync=False, blocking=True)

# furhat.say(text="Imam hatipler kapatilsin", blocking=True)
# furhat.say(text="Kafana sikacagim gunu bekle hahaha", blocking=True)
# furhat.gesture(name="Wink")

# furhat.say(text="Now I will pause delay(2000) yes")
# furhat.say(text="{Now I will} +  delay(2000) + pause yes", blocking=True)
# print(furhat.get_gestures())

furhat.say_stop()

# furhat.say(text="wahhhhh death", blocking=True)

# furhat.gesture(body={
#     "frames": [
#         {
#             "time": [
#                 2
#             ],
#             "params": {
#                 "BLINK_LEFT": 1.0
#             }
#         },
#         {
#             "time": [
#                 3
#             ],
#             "params": {
#                 "reset": True
#             }
#         }
#     ],
#     "class": "furhatos.gestures.Gesture"
#     })
# # furhat.gesture(body={
# #     "frames": [
#         {
#             "time": [
#                 4
#             ],
#             "params": {
#                 "LOOK_LEFT_LEFT": 1.0,
#                 "LOOK_RIGHT_RIGHT": 1.0
#             }
#         },
#         {
#             "time": [
#                 8
#             ],
#             "params": {
#                 "LOOK_LEFT_RIGHT": 1.0,
#                 "LOOK_RIGHT_LEFT": 1.0,

#             }
#         }
#     ],
#     "class": "furhatos.gestures.Gesture"
#     })
# furhat.set_led(red=200, green=50, blue=50)
#furhat.set_face(mask="adult", character="Omar")


# users = furhat.get_users()
# print(users)
# usr1 = str(users[0]).replace("'", '"')
# print(type(usr1))
# print(usr1)
# usr1 = json.loads(usr1)

# print(usr1["id"])
# furhat.attend(user="OTHER")
# furhat.attend(location="-0.4, -0.27, 0.2")

# users_dict = json.loads(users)

# print(users_dict[0]["id"])

# furhat.attend(userid = "virtual-user-1")
# sleep(2)
# furhat.attend(userid = "virtual-user-0")

# furhat.attend(user="RANDOM")

# answer = furhat.listen()

# print("ANSWER:::")
# print(answer.message)