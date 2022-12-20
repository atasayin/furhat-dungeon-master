import mediapipe as mp
import cv2 as cv
from handlandmark import HandLandmark
from hand import Hand

class HandViewer:
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.vid = cv.VideoCapture(0)
        self.hands = []

    def compute_direction_hands(self, hls, handedness):
        if handedness[0].classification[0].label == "Left":
            return hls[0], hls[1]
        else:
            return hls[1], hls[0]

    def capture_hands(self):
        with self.mp_hands.Hands(model_complexity=0,
                                 min_tracking_confidence=0.5,
                                 min_detection_confidence=0.5,
                                 max_num_hands=4) as hands:
            success = False
            while not success:
                success, frame = self.vid.read()

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = cv.flip(frame, 1)
            hands_results = hands.process(frame)

            for i, hand_landmarks in enumerate(hands_results.multi_hand_landmarks):
                hand = Hand()
                hand.landmarks = hand_landmarks.landmark
                hand.label = hands_results.multi_handedness[i].classification[0].label
                self.hands.append(hand)        

h = HandViewer()
h.capture_hands()
print(len(h.get_hand_point_coordinates()))
print(h.get_multi_handedness())
print(h.hands[0].__str__())
print(h.hands[1].__str__())

