class Turn:
    def __init__(self) -> None:
        self.turn_type = None
        self.hope_change = 0
        self.discontent_change = 0
        self.rebellion_point_change = 0
        self.attack_territory = None
        self.maze_destination = None
        self.milestone_requested = None
        self.powerup_requested = None
        self.success = False
    

    def reset_turn(self):
        self.turn_type = None
        self.hope_change = 0
        self.discontent_change = 0
        self.rebellion_point_change = 0
        self.attack_territory = None
        self.maze_destination = None
        self.milestone_requested = None
        self.powerup_requested = None
        self.success = False
    
    
    def get_changes(self):
        return self.hope_change, self.discontent_change, self.rebellion_point_change

    
