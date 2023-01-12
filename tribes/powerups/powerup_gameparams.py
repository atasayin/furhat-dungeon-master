from .powerup_base import PowerupBase

class PowerupGameParams(PowerupBase):
    def __init__(self, effects, game_params) -> None:
        PowerupBase.__init__(self)
        self.effects = effects
        self.game_params = game_params
            
    def use(self):
        for param,effect in self.effects.items():
            self.game_params[param] *= effect
            print(self.game_params[param])