import mediapipe as mp
import cv2 as cv

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
vid = cv.VideoCapture(0)
clock = 0

with mp_hands.Hands(model_complexity=0,
                        min_tracking_confidence=0.5,
                        min_detection_confidence=0.5) as hands:
while True:
    ret, frame = vid.read()

    if not ret or frame is None:
        break

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.flip(frame, 1)
    results = hands.process(frame)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    round_result = -1

    
    

vid.release()
cv.destroyAllWindows()
