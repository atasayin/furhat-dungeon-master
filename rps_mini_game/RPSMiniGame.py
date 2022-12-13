import cv2 as cv
import mediapipe as mp
from furhat_remote_api import FurhatRemoteAPI
from .drawer import Drawer
from .moves import Moves
from .handpoints import HandPoints
from .results import RPSResults


N_POINTS_PER_FINGER = 4
DIST_EPSILON_COEF = 0.8  # TEST THIS


class RPSMiniGame():
    def __init__(self, win_count=3, drawer=None):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.vid = cv.VideoCapture(0)
        self.win_count = win_count
        self.clock = 0
        self.pleft_score = 0
        self.pleft_move = -1
        self.pright_score = 0
        self.pright_move = -1
        self.hist = []
        self.drawer = drawer
        self.is_draw = drawer is not None
        self.furhat = FurhatRemoteAPI("localhost")

    def compute_hand_move(self, hand_landmarks):
        landmarks = hand_landmarks.landmark
        is_finger_down = {}  # finger_index -> true, false
        def dist(x1, x2, y1, y2, z1, z2): return (
            x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

        for finger in range(HandPoints.INDEX_FINGER_MCP, HandPoints.PINKY_TIP, N_POINTS_PER_FINGER):
            mcp_distance = dist(landmarks[finger].x, landmarks[HandPoints.WRIST_NUMBER].x, landmarks[finger].y,
                                landmarks[HandPoints.WRIST_NUMBER].y, landmarks[finger].z, landmarks[HandPoints.WRIST_NUMBER].z)
            tip_distance = dist(landmarks[finger + 3].x, landmarks[HandPoints.WRIST_NUMBER].x, landmarks[finger + 3].y,
                                landmarks[HandPoints.WRIST_NUMBER].y, landmarks[finger + 3].z, landmarks[HandPoints.WRIST_NUMBER].z)
            is_finger_down[finger] = mcp_distance > tip_distance * \
                DIST_EPSILON_COEF  # TEST THIS

        if all([down for down in is_finger_down.values()]):
            return Moves.ROCK_INDEX
        elif is_finger_down[HandPoints.RING_FINGER_MCP] or is_finger_down[HandPoints.PINKY_MCP]:
            return Moves.SCISSOR_INDEX
        else:
            return Moves.PAPER_INDEX

    def compute_direction_hands(self, hls, handedness):
        if handedness[0].classification[0].label == "Left":
            return hls[0], hls[1]
        else:
            return hls[1], hls[0]

    def compute_result_round(self, pleft_move, pright_move):
        if pleft_move == pright_move:
            return RPSResults.TIE_RESULT
        elif pleft_move == Moves.PAPER_INDEX and pright_move == Moves.ROCK_INDEX:
            return RPSResults.PLEFT_WIN_RESULT
        elif pleft_move == Moves.ROCK_INDEX and pright_move == Moves.SCISSOR_INDEX:
            return RPSResults.PLEFT_WIN_RESULT
        elif pleft_move == Moves.SCISSOR_INDEX and pright_move == Moves.PAPER_INDEX:
            return RPSResults.PLEFT_WIN_RESULT
        else:
            return RPSResults.PRIGHT_WIN_RESULT

    def play_game(self):
        with self.mp_hands.Hands(model_complexity=0,
                                 min_tracking_confidence=0.5,
                                 min_detection_confidence=0.5) as hands:
            while True:
                ret, frame = self.vid.read()

                if not ret or frame is None:
                    break

                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame = cv.flip(frame, 1)
                results = hands.process(frame)
                frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
                round_result = -1

                if 0 < self.clock < 10:
                    success = True
                elif self.clock < 20:
                    print("3...")
                elif self.clock == 20:
                    self.furhat.say(text="Rock", blocking=True)
                elif self.clock < 25:
                    print("2...")
                elif self.clock == 25:
                    self.furhat.say(text="Paper", blocking=True)
                elif self.clock < 30:
                    print("1...")
                elif self.clock == 35:
                    self.furhat.say(text="Scissor", blocking=True)
                elif self.clock < 40:
                    print("GO!")
                elif self.clock == 40:
                    self.furhat.say(text="Go!", blocking=True)
                elif self.clock == 45:
                    hls = results.multi_hand_landmarks
                    handedness = results.multi_handedness
                    if hls and len(hls) == 2:
                        pleft_landmarks, pright_landmarks = self.compute_direction_hands(
                            hls, handedness)
                        self.pleft_move = self.compute_hand_move(
                            pleft_landmarks)
                        self.pright_move = self.compute_hand_move(
                            pright_landmarks)
                    else:
                        success = False
                elif self.clock < 60:
                    if success:
                        round_result = self.compute_result_round(
                            self.pleft_move, self.pright_move)
                        self.hist.append(round_result)
                        print(round_result)

                        if round_result == RPSResults.PLEFT_WIN_RESULT:
                            self.pleft_score += round_result

                        elif round_result == RPSResults.PRIGHT_WIN_RESULT:
                            self.pright_score += round_result

                        if self.pleft_score == - self.win_count:
                            self.furhat.say(
                                text="Left Player Wins!", blocking=True)
                            print("Left Player Wins")
                            print(self.hist)
                            return -1
                        if self.pright_score == self.win_count:
                            self.furhat.say(
                                text="Right Player Wins!", blocking=True)
                            print("Right Player Wins")
                            print(self.hist)
                            return 1
                        success = False
                    else:
                        pass
                        #furhat.say(text="I couldn't caught that")

                self.clock = (self.clock + 1) % 60

                if self.is_draw:
                    self.drawer.draw_results(frame, self, results)

                if cv.waitKey(1) == ord('q'):
                    break

        self.vid.release()
        cv.destroyAllWindows()
