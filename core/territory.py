class Territory:
    def __init__(self, name,size,owner=None) -> None:
        if owner is None:
            self.owner = 'Vahdettin'
        else:
            self.owner = owner
        self.name = name
        if size is None:
            self.size = 5
        else:
            self.size = size
        self.passive_generation = self.size*1.5

    def conquer(self):
        self.owner = 'Player'

    def generate_passif_income(self,t_list):
        total_income = 0
        for territory in t_list.values():
            if territory is not None:
                total_income += territory.passive_generation
        return total_income

    def losing_territory(self, t_list,losing_index):
        t_list[losing_index] = None
        return t_list




