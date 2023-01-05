from .tribe import Tribe
import powerups

class TribeManager:
    def __init__(self,game_params):
        self.locked_tribes = []
        self.unlocked_tribes = []
        
        self.add_tribes(game_params)

    def add_tribes(self,game_params):
        self.locked_tribes.append(Tribe("comp", powerups.PowerupGameParams({"discontent_gain":1.25},game_params)))

    def find_unlocked_tribe(self,name):
        for tribe in self.unlocked_tribes:
            if tribe.name == name:
                return tribe
        return None

    def find_locked_tribe(self,name):
        for tribe in self.locked_tribes:
            if tribe.name == name:
                return tribe
        return None

    def is_already_conquered(self,name):
        tribe = self.find_locked_tribe(name)     
        return tribe == None

    def conquer_tribe(self,name):
        tribe = self.find_locked_tribe(name)
        self.locked_tribes.remove(tribe)
        self.unlocked_tribes.append(tribe)  
        return tribe