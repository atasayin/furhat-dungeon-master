from .onetime_milestone import OneTimeMilestone

class LowerExile(OneTimeMilestone):
    def __init__(self):
        OneTimeMilestone.__init__(self,name="lower excile",cost=30)

    def apply_ability(self, game_params):
        if not self.is_used:
            game_params["hope"] += 40
            game_params["discontent"] -= 40
            self.is_used = True