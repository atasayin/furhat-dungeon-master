from furhat_remote_api import FurhatRemoteAPI
from time import sleep

furhat = FurhatRemoteAPI("localhost")

# furhat.say(text="Imam hatipler kapatilsin", blocking=True)
# furhat.say(text="Kafana sikacagim gunu bekle hahaha", blocking=True)
furhat.gesture(name="BigSmile")

furhat.say(text="it is depent of shaps. ", blocking=True)
furhat.say(text="microphone not working", blocking=True)
furhat.say(text="shape", blocking=True)


print(furhat.get_users())

# furhat.attend(userid = "virtual-user-1")
# sleep(2)
# furhat.attend(userid = "virtual-user-0")

# furhat.attend(user="random")

answer = furhat.listen()

print("ANSWER:::")
# print(answer.message)