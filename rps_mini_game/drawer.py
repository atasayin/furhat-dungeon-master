import cv2 as cv
import mediapipe as mp
from .moves import Moves

class Drawer():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def draw_hands(self,frame, results, hand_landmarks):
        if hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame,
                                        hand_landmarks,
                                        self.mp_hands.HAND_CONNECTIONS,
                                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                                        self.mp_drawing_styles.get_default_hand_connections_style())

    def draw_results(self,frame,rps, mp_results):
        hand_landmarks = mp_results.multi_hand_landmarks
        clock = rps.clock
        pleft_score = rps.pleft_score 
        pright_score = rps.pright_score 
        hist = rps.hist
        pleft_move = rps.pleft_move
        pright_move = rps.pright_move
        
        self.draw_hands(frame, mp_results, hand_landmarks)

        pleft_move_text = pright_move_text = ""
        gameText = ""

        if 0 < clock < 20:
            gameText = "Ready?"
        elif clock < 30:
            gameText = "3..."
        elif clock < 40:
            gameText = "2..."
        elif clock < 50:
            gameText = "1..."
        elif clock < 60:
            gameText = "GO!"
        elif clock < 100:
            if pleft_move == Moves.ROCK_INDEX:
                pleft_move_text = "Rock"
            elif pleft_move == Moves.SCISSOR_INDEX:
                pleft_move_text = "Scissor"
            elif pleft_move == Moves.PAPER_INDEX:
                pleft_move_text = "Paper"
            else:
                pleft_move_text = "Wrong Move"

            if pright_move == Moves.ROCK_INDEX:
                pright_move_text = "Rock"
            elif pright_move == Moves.SCISSOR_INDEX:
                pright_move_text = "Scissor"
            elif pright_move == Moves.PAPER_INDEX:
                pright_move_text = "Paper"
            else:
                pright_move_text = "Wrong Move"

            gameText = pleft_move_text + " vs " + pright_move_text + " --> "  + "Current Score: " + str(-pleft_score) + " vs " + str(pright_score)

        cv.putText(frame, f"Clock {clock}", (50, 50), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv.LINE_AA)
        cv.putText(frame, gameText, (50, 80), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow("rock-paper-scissor", frame)

