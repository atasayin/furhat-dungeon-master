from .powerup_base import PowerupBase

class PowerupTerritory(PowerupBase):
    def __init__(self, name, territorys) -> None:
        super.__init__(self,name)
        self.territorys = territorys