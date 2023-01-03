from .pasif_milestone import PasifMilestone

class Salicaz(PasifMilestone):
    def __init__(self):            
        PasifMilestone.__init__(self,name="salicaz",cost=1)

    def apply_ability(self,game_params):
        game_params["hope"] += 10 
