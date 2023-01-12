from furhat_remote_api import FurhatRemoteAPI
import json
import random
import serial 


positive = ["yes", "sure", "i do", "of course", "alright", "i will", "yes i will", "ok"]
turn_questions = ["how would you like to proceed?", "what is your next move?", "so, what now?",
                    "what will you do this time?"]
# port = "/dev/cu.usbserial-0001"
# ard = serial.Serial(port,9600,timeout=5)
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

    def say_one_of_them(self, texts, blocking=True):
        text = random.choice(texts)
        self.say(text, blocking=blocking)
    
    def ask_question(self, text = None, blocking=True):
        if text:
            self.furhat.say(text=text,blocking=blocking)
        return str(self.furhat.listen().message).lower()
    
    def ask_one_of_them(self, texts, blocking=True):
        text = random.choice(texts)
        return self.ask_question(text,blocking=blocking)

    def listen_stop(self):
        self.furhat.listen_stop()


    def look_at_screen(self):
        self.furhat.attend(location="-0.4, -0.27, 0.2")

    
    def look_at_player(self, player_id):
        self.furhat.attend(userid=player_id)

    def look_at_other_player(self):
        self.furhat.attend(user="OTHER")

    def get_volunteer_status(self, player1, player2):
        self.look_at_player(player1)
        self.say("Player 1, do you want to be the captain?")
        answer = str(self.furhat.listen().message).lower()
        print(answer)
        volunteer1, volunteer2 = False, False
        if answer in positive or "yes" in answer:
            volunteer1 = True
            self.say("Alright then. We have our first volunteer.")
        else:
            self.say("OK, let's see if your friend will volunteer.")

        self.look_at_player(player2)
        if volunteer1:
            print("Volunteer 1")
            self.say("Would you also want to volunteer to be the captain?")
        else:
            self.say("We might need a captain. Will you take the responsibility?")

        answer = str(self.furhat.listen().message).lower()

        if answer in positive or "yes" in answer:
            print("Volunteer 2")
            volunteer2 = True
            if volunteer1:
                self.say("Wow. We have two volunteers for role, eh. There has to be a solution for this.")
                return volunteer1, volunteer2
            else:
                self.say("Alright then. Since you are the sole volunteer. You will be our captain from now on.")
        else:
            self.look_at_player(player1)
            if volunteer1:
                self.say("Alright then. Since you are the sole volunteer. You will be our captain from now on.")
            else:
                self.say("Alright. Since we need a captain. I will select one of you randomly.")
                rand = random.choice(["Player 1", "Player 2"])
                print(rand)
                if rand == "Player 1":
                    volunteer1 = True
                    self.say("Player 1. From now on, you are the captain of this rebellion.")
                else:
                    volunteer2 = True
                    self.look_at_player(player2)
                    self.say("Player 2. From now on, you are the captain of this rebellion.")


        
        return volunteer1, volunteer2

    
    def define_the_roles(self, captain, assistant):
        self.look_at_player(captain)
        capt = """Oh captain, my captain. The responsibility you are about to take on is 
        one that is hard to bear. The future of many students are on your shoulders. 
        You must lead wisely."""
        self.say(capt)

        self.look_at_player(assistant)
        ass = """ No rebellion can succeed without proper motivation, patience, and resilience. 
        Throughout the game, you must not let the hope replenish.
        """
        self.say(ass)


    def find_the_player_on_the_right(self, player1, player2):
        users = self.furhat.get_users()
        
        usr1 = json.loads(str(users[0]).replace("'", '"'))
        usr2 = json.loads(str(users[1]).replace("'", '"'))

        if usr1["location"]["x"] > usr2["location"]["x"]:
            if usr1["id"] == str(player1):
                player = player1
            else:
                player = player2

        else:
            if usr2["id"] == str(player1):
                player = player1
            else:
                player = player2
        

        return player

    def ask_turns(self):
        choice = random.choice(turn_questions)
        self.say(choice)
        

    def get_passive_selection(self):
        self.say()

    def get_gesture(self,gesture):
        self.furhat.gesture(name=gesture)

    def shaka(self):
        print("I DIDN\'T know you were cool like that...")
        self.say("I DIDN\'T know you were cool like that...")

        # ard.write(b"a")








