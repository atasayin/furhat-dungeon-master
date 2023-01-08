from .tribe import Tribe
import tribes.powerups as powerups

class TribeManager:
    def __init__(self,game_params):
        self.locked_tribes = []
        self.unlocked_tribes = []
        self.unused_powerup_tribes = []
        self.used_powerup_tribes = []
        
        self.add_tribes(game_params)

    def add_tribes(self,game_params):
        self.locked_tribes.append(Tribe("computer", powerups.PowerupGameParams({"discontent_gain":1.25},game_params)))

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

    def find_unused_powerup_tribe(self,name):
        for tribe in self.unused_powerup_tribes:
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
        self.unused_powerup_tribes.append(tribe)
        return tribe

    def use_powerup_tribe(self,name):
        tribe = self.find_unused_powerup_tribe(name)
        tribe.powerup.use()
        self.unused_powerup_tribes.remove(tribe)
        self.used_powerup_tribes.append(tribe)