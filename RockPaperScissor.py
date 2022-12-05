import cv2 as cv
import mediapipe as mp
from furhat_remote_api import FurhatRemoteAPI

WRIST_NUMBER = 0
INDEX_FINGER_MCP = 5
RING_FINGER_MCP = 13
PINKY_MCP = 17
PINKY_TIP = 20
N_POINTS_PER_FINGER = 4
DIST_EPSILON_COEF = 0.8  # TEST THIS

ROCK_INDEX = 0
SCISSOR_INDEX = 1
PAPER_INDEX = 2

PLEFT_WIN_RESULT = -1
TIE_RESULT = 0
PRIGHT_WIN_RESULT = 1

WIN_COUNT = 3

def draw_hands(hand_landmarks):
    if hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,
                                      hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())

def draw_results(frame,pleft_move, pright_move, result, pleft_score, pright_score, clock, hand_landmarks):
    draw_hands(hand_landmarks)

    pleft_move_text = pright_move_text = ""
    round_text = ""
    gameText = ""

    if 0 < clock < 20:
        gameText = "Ready?"
    elif clock < 30:
        gameText = "3..."
        # furhat.say(text="Rock")
    elif clock < 40:
        gameText = "2..."
        # furhat.say(text="Paper")
    elif clock < 50:
        gameText = "1..."
        # furhat.say(text="Scissor")
    elif clock < 60:
        gameText = "GO!"
    elif clock < 100:
        if pleft_move == ROCK_INDEX:
            pleft_move_text = "Rock"
        elif pleft_move == SCISSOR_INDEX:
            pleft_move_text = "Scissor"
        elif pleft_move == PAPER_INDEX:
            pleft_move_text = "Paper"
        else:
            pleft_move_text = "Wrong Move"
        if pright_move == ROCK_INDEX:
            pright_move_text = "Rock"
        elif pright_move == SCISSOR_INDEX:
            pright_move_text = "Scissor"
        elif pright_move == PAPER_INDEX:
            pright_move_text = "Paper"
        else:
            pright_move_text = "Wrong Move"

        if result == PLEFT_WIN_RESULT:
            round_text = "Left Player Wins"
        elif result == PRIGHT_WIN_RESULT:
            round_text = "Right Player Wins"
        elif result == TIE_RESULT:
            round_text = "Tie"
        else:
            round_text = "Error"

        gameText = pleft_move_text + " vs " + pright_move_text + "->" + round_text + "Current Score: " + str(-pleft_score) + " vs " + str(pright_score)

    cv.putText(frame, f"Clock {clock}", (50, 50), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv.LINE_AA)
    cv.putText(frame, gameText, (50, 80), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2, cv.LINE_AA)


    cv.imshow("rock-paper-scissor", frame)

def compute_hand_move(hand_landmarks):
    landmarks = hand_landmarks.landmark
    is_finger_down = {}  #finger_index -> true, false

    for finger in range(INDEX_FINGER_MCP, PINKY_TIP, N_POINTS_PER_FINGER):
        dist = lambda x1,x2,y1,y2,z1,z2 : (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
        mcp_distance = dist(landmarks[finger].x, landmarks[WRIST_NUMBER].x,landmarks[finger].y, landmarks[WRIST_NUMBER].y,landmarks[finger].z, landmarks[WRIST_NUMBER].z)
        tip_distance = dist(landmarks[finger + 3].x, landmarks[WRIST_NUMBER].x,landmarks[finger + 3].y, landmarks[WRIST_NUMBER].y, landmarks[finger + 3].z, landmarks[WRIST_NUMBER].z)
        is_finger_down[finger] = mcp_distance > tip_distance * DIST_EPSILON_COEF #TEST THIS

    if all([down for down in is_finger_down.values()]):
        return ROCK_INDEX
    elif is_finger_down[RING_FINGER_MCP] or is_finger_down[PINKY_MCP]:
        return SCISSOR_INDEX
    else:
        return PAPER_INDEX

def compute_direction_hands(hls, handedness):
    if handedness[0].classification[0].label == "Left":
        return hls[0], hls[1]
    else:
        return hls[1], hls[0]

def compute_result_round(pleft_move, pright_move):
    if pleft_move == pright_move:
        return TIE_RESULT
    elif pleft_move == PAPER_INDEX and pright_move == ROCK_INDEX:
        return PLEFT_WIN_RESULT
    elif pleft_move == ROCK_INDEX and pright_move == SCISSOR_INDEX:
        return PLEFT_WIN_RESULT
    elif pleft_move == SCISSOR_INDEX and pright_move == PAPER_INDEX:
        return PLEFT_WIN_RESULT
    else:
        return PRIGHT_WIN_RESULT



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

vid = cv.VideoCapture(0)

clock = 0
pleft_move = pright_move = -1
gameText = ""
success = True

pleft_score = pright_score = 0
hist = []

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
        result = -1
        if 0 < clock < 20:
            success = True
            pass
        elif clock < 30:
            # furhat.say(text="Rock")
            print("3...")
        elif clock < 40:
            # furhat.say(text="Paper")
            print("2...")
        elif clock < 50:
            # furhat.say(text="Scissor")
            print("1...")
        elif clock < 60:
            print("GO!")
            # furhat.say(text="Go!") ?
        elif clock == 60:
            hls = results.multi_hand_landmarks
            handedness = results.multi_handedness
            if hls and len(hls) == 2:
                pleft_landmarks, pright_landmarks = compute_direction_hands(hls, handedness)
                pleft_move = compute_hand_move(pleft_landmarks)
                pright_move = compute_hand_move(pright_landmarks)
            else:
                success = False
        elif clock < 100:
            if success:
                result = compute_result_round(pleft_move,pright_move)
                hist.append(result)
                print(result)
                if result == PLEFT_WIN_RESULT:
                    pleft_score += result
                elif result == PRIGHT_WIN_RESULT:
                    pright_score += result
                if pleft_score == -WIN_COUNT:
                    print("Left Player Wins")
                    print(hist)
                    break
                if pright_score == WIN_COUNT:
                    print("Right Player Wins")
                    print(hist)
                    break
                success = False
            else:
                pass
                #furhat.say(text="I couldn't caught that")

        draw_results(frame, pleft_move, pright_move, result, pleft_score, pright_score, clock, results.multi_hand_landmarks)

        clock = (clock + 1) % 100

        if cv.waitKey(1) == ord('q'):
            break


vid.release()
cv.destroyAllWindows()




