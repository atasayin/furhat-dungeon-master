from .tribe import Tribe
import tribes.powerups as powerups

class TribeManager:
    def __init__(self):
        self.locked_tribes = []
        self.unlocked_tribes = []
        self.unused_powerup_tribes = []
        self.used_powerup_tribes = []
        
        self.add_tribes()

    def add_tribes(self):
        self.locked_tribes.append(Tribe("computer", powerups.PowerupGameParams({"type": "mult","passive_rp_income":1.25})))
        self.locked_tribes.append(Tribe("mava", powerups.PowerupGameParams({"type": "mult","discontent_gain":0.75})))
        self.locked_tribes.append(Tribe("mech", powerups.PowerupGameParams({"type": "sum","territory_defense_boos":1})))
        self.locked_tribes.append(Tribe("electronic", powerups.PowerupGameParams({"type": "mult","territory_attack_boos":1})))
        self.locked_tribes.append(Tribe("medicine", powerups.PowerupGameParams({"type": "mult","hope_gain":1.25})))

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
        tribe = self.find_unlocked_tribe(name)     
        return tribe 

    def is_power_available(self,name):
        tribe = self.find_unused_powerup_tribe(name)     
        return tribe 

    def conquer_tribe(self,name):
        tribe = self.find_locked_tribe(name)
        self.locked_tribes.remove(tribe)
        self.unlocked_tribes.append(tribe)  
        self.unused_powerup_tribes.append(tribe)
        return tribe

    def use_powerup_tribe(self,name, game_params):
        tribe = self.find_unused_powerup_tribe(name)
        tribe.powerup.use(game_params)
        self.unused_powerup_tribes.remove(tribe)
        self.used_powerup_tribes.append(tribe)
        return tribe.powerup.use_feedback_text