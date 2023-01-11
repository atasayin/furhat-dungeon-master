from .pasif_milestone import PasifMilestone

class OpenSportFields(PasifMilestone):
    def __init__(self):            
        PasifMilestone.__init__(self,name="open sport fields",cost=50)

    def apply_ability(self,game_params):
        #game_params["def_rng"] += 2
        print("open sport fields def rng boost")
