class Hand:
    def __init__(self) -> None:
        self.label = None
        self.landmarks = None

    def __str__(self) -> str:
        return f"label: {self.label}\nlandmarks: {self.landmarks}"
