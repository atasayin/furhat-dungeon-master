from furhat_remote_api import FurhatRemoteAPI
import json

class FurhatDriver:
    def __init__(self) -> None:
        self.furhat = FurhatRemoteAPI("localhost")
        self.test_furhat()

    



    def test_furhat(self):
        self.furhat.say(text="Keys are under the sofa.")

    
    def get_user_ids(self):
        users = self.furhat.get_users()
        if len(users) < 2:
            print("LESS THAN TWO PLAYERS PRESENT!")
            return None
        usr1 = json.loads(str(users[0]).replace("'", '"'))["id"]
        usr2 = json.loads(str(users[1]).replace("'", '"'))["id"]

        return (usr1, usr2)

