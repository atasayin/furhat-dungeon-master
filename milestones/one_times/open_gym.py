from .onetime_milestone import OneTimeMilestone

class OpenGym(OneTimeMilestone):
    def __init__(self):
        OneTimeMilestone.__init__(self,name="open gym",cost=50)

    def apply_ability(self, game_params):
         if not self.is_used:
            #game_params["con_rng"] += 2
            print("open_gym conquest rng boost")
            self.is_used = True