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

