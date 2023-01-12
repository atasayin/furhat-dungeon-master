
# import mediapipe as mp
# import cv2 as cv

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands
# vid = cv.VideoCapture(0)
# clock = 0

# with mp_hands.Hands(model_complexity=0,
#                         min_tracking_confidence=0.5,
#                         min_detection_confidence=0.5) as hands:
# while True:
#     ret, frame = vid.read()

#     if not ret or frame is None:
#         break

#     frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#     frame = cv.flip(frame, 1)
#     results = hands.process(frame)
#     frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
#     round_result = -1
import os 

cwd = os.getcwd()
im = os.path.join(cwd, "images")
print(os.path.join(im, "furhat.png"))
    

#     def dothework(self):
#         while run:

#             self.win.fill((255,255,255))
#             self.clock.tick(120)


            
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#             deg += 0.03

#             text = self.font.render("GAMEEEE", True, (0,0,0))
#             text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2  + math.sin(deg) * 40 - 50))
#             self.win.blit(text, text_rect)
#             pygame.display.update()

#             if deg > 40:
#                 return

# import multiprocessing



# print("Number of cpu : ", multiprocessing.cpu_count())
