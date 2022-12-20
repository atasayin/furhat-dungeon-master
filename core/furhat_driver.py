from furhat_remote_api import FurhatRemoteAPI
import json

class FurhatDriver:
    def __init__(self) -> None:
        self.furhat = FurhatRemoteAPI("localhost")
        self.test_furhat()

    
    def test_furhat(self):
        self.furhat.say(text="I am online")

    
    def get_user_ids(self):
        users = self.furhat.get_users()
        if len(users) < 2:
            print("LESS THAN TWO PLAYERS PRESENT!")
            return None
        usr1 = json.loads(str(users[0]).replace("'", '"'))["id"]
        usr2 = json.loads(str(users[1]).replace("'", '"'))["id"]

        return (usr1, usr2)

    
    def introduce_players(self, player_ids):
        print(player_ids[0])
        self.look_at_player(player_ids[0])
        self.say("Player 1, welcome to our game.")

        self.look_at_player(player_ids[1])
        self.say("Player 2, welcome to our game.")



    def say(self, text, blocking=True):
        self.furhat.say(text=text, blocking=blocking)


    def look_at_screen(self):
        self.furhat.attend(location="-0.4, -0.27, 0.2")

    
    def look_at_player(self, player_id):
        self.furhat.attend(userid=player_id)

    def look_at_other_player(self):
        self.furhat.attend(user="OTHER")

  



