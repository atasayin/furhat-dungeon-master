from .powerup_base import PowerupBase

class PowerupGameParams(PowerupBase):
    def __init__(self, effects) -> None:
        PowerupBase.__init__(self)
        self.effects = effects
            
    def use(self,game_params):
        for param,effect in self.effects.items():
            game_params[param] *= effect
        