from .powerup_base import PowerupBase

class PowerupTerritory(PowerupBase):
    def __init__(self, territorys) -> None:
        PowerupBase.__init__(self)
        self.territorys = territorys