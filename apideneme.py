from furhat_remote_api import FurhatRemoteAPI
from time import sleep
import json

furhat = FurhatRemoteAPI("localhost")


while True:
    furhat.say(text="say it", blocking=True)
    furhat.listen()
# furhat.gesture(name="BigSmile")

# furhat.set_led(red=200, green=50, blue=50)
#furhat.set_face(mask="adult", character="Omar")

# users = furhat.get_users()
# print(users)
# usr1 = str(users[0]).replace("'", '"')
# print(type(usr1))
# print(usr1)
# usr1 = json.loads(usr1)

# print(usr1["id"])
# furhat.attend(user="CLOSEST")
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