from .powerup_base import PowerupBase

class PowerupGameParams(PowerupBase):
    def __init__(self, effects) -> None:
        PowerupBase.__init__(self)
        self.effects = effects
        boost = list(effects.keys())[1].replace("_", " ")
        self.use_feedback_text = f"You have gain {boost} boost"
            
    def use(self,game_params):
        if self.effects["type"] == "mult":
            for param,effect in self.effects.items():
                if param == "type":
                    continue
                game_params[param] *= effect

        elif self.effects["type"] == "sum":
            for param,effect in self.effects.items():
                if param == "type":
                    continue
                game_params[param] += effect
