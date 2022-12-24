from handlandmark import HandLandmark
class Hand:
    def __init__(self) -> None:
        self.label = None
        self.landmarks = None

    def get_coordiantes_finger_point(self,hand_point):
        return self.landmarks[hand_point]
    
    def get_wrist_coordiantes(self):
        return self.get_coordiantes_finger_point(HandLandmark.WRIST)

    def __str__(self) -> str:
        return f"label: {self.label}\nlandmarks: {self.landmarks}"
