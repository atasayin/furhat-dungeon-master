class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.locked_territorys = None
        self.unlocked_territorys = None
    
    def add(self,powerup):
        self.powerups.append(powerup)

    def remove(self,powerup):
        self.powerups.remove(powerup)

    def find_powerup(self,name):
        for power in self.powerups:
            if power.name == name:
                return power
        return None