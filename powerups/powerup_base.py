class PowerupBase:
    def __init__(self, name) -> None:
        self.name = name
        self.is_used = False
        self.use_feedback_text = ""