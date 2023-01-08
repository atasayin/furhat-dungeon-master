class Tribe:
    def __init__(self,name, powerup):
        self.name = name
        self.powerup = powerup
    
    def gain_powerup(self):
        return self.powerup