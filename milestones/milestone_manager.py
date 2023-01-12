import milestones.one_times as one_times
import milestones.pasifs as pasifs

class MilestoneManager:
    def __init__(self):
        self.locked_oneTimes = []
        self.locked_pasifs = []
        self.unlocked_oneTimes = []
        self.unlocked_pasifs = []

        self.add_milestones()

    def add_milestones(self):
        self.locked_oneTimes.append(one_times.LowerExile())
        self.locked_oneTimes.append(one_times.OpenGym())
        self.locked_oneTimes.append(one_times.RemoveDressCode())
        
        self.locked_pasifs.append(pasifs.Salicaz())
        #self.locked_pasifs.append(pasifs.OpenSportFields())
        self.locked_pasifs.append(pasifs.StudentClubs())

    def find_unlocked_milestone(self,name):
        # for pasif, onetime in zip(self.unlocked_pasifs,self.unlocked_oneTimes):
        #     if pasif.name == name:
        #         return pasif
        #
        #     if onetime.name == name:
        #         return onetime
        # return None
        for pasif in self.unlocked_pasifs:
            if pasif.name == name:
                return pasif
        for onetime in self.unlocked_oneTimes:
            if onetime.name == name:
                return onetime
        return None

    def find_locked_milestone(self,name):
        #for pasif, onetime in zip(self.locked_pasifs,self.locked_oneTimes):
        #     print(pasif,onetime)
        #     if pasif.name == name:
        #         return pasif
        #
        #     if onetime.name == name:
        #         return onetime
        # return None
        for pasif in self.locked_pasifs:
            if pasif.name == name:
                return pasif
        for onetime in self.locked_oneTimes:
            if onetime.name == name:
                return onetime
        return None

    def is_already_bought(self,name):
        ms = self.find_locked_milestone(name)     
        return ms == None

    def is_money_enough(self,name,money):
        ms = self.find_locked_milestone(name)     
        if ms.cost > money:
                return False
        return True

    def buy_milestone(self,name):
        cost = 0
        for pasif in self.locked_pasifs:
            if pasif.name == name:
                self.locked_pasifs.remove(pasif)
                self.unlocked_pasifs.append(pasif)
                return pasif.cost
            
        for onetime in self.locked_oneTimes:
            if onetime.name == name:
                self.locked_oneTimes.remove(onetime)
                self.unlocked_oneTimes.append(onetime)
                return onetime.cost

        return None
            
    
    def apply_one_time(self,name,game_params):
        for onetime in self.locked_oneTimes:
            if onetime.name == name:
                onetime.apply_ability(game_params)
                
    def apply_pasifs(self,game_params):
        for pasif in self.unlocked_pasifs:
            pasif.apply_ability(game_params)