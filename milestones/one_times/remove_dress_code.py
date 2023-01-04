from .onetime_milestone import OneTimeMilestone

class RemoveDressCode(OneTimeMilestone):
    def __init__(self):
        OneTimeMilestone.__init__(self,name="remove dress code",cost=3)

    def apply_ability(self, game_params):
         if not self.is_used:
            game_params["discontent"] -= 60
            self.is_used = True