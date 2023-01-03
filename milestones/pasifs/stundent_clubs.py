from .pasif_milestone import PasifMilestone

class StudentClubs(PasifMilestone):
    def __init__(self):            
        PasifMilestone.__init__(self,name="student clubs",cost=2)

    def apply_ability(self,game_params):
        game_params["hope"] += 10 
        game_params["discontent"] -= 10 