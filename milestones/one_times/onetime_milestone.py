from ..milestonebase import Milestone

class OneTimeMilestone(Milestone):
    def __init__(self,name,cost):
        Milestone.__init__(self,name,cost)
        self.is_used = False