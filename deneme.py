import pygame
import math
from CONSTANTS import *

class Deneme():
    def __init__(self, win, clock, font) -> None:
        self.win = win
        self.clock = clock
        self.font = font
    
    def dothework(self):
        while run:

            if game_state is "intro":
                self.win.fill((255,255,255))
                mousepos = pygame.mouse.get_pos()
                self.clock.tick(120)


                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                deg += 0.03

                text = self.font.render("Furhat", True, (0,0,0))
                text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2  + math.sin(deg) * 40 - 50))
                self.win.blit(text, text_rect)
                pygame.display.update()