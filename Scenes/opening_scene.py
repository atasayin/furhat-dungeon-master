from .scene_base import SceneBase
import pygame
from Util.text_manup import wrapline
import CONSTANTS
from .game_story import story
class OpeningScene(SceneBase):
    def __init__(self, furhat):
        SceneBase.__init__(self)
        self.next = self
        self.font = pygame.font.Font("/Users/deniz/Desktop/Furh/furhat-dungeon-master/fonts/starjedi.ttf", 50)
        self.text = story
        self.rect_texts = wrapline(self.text, self.font, CONSTANTS.WIDTH)
        self.slide = 0
        self.school_photo = pygame.image.load("/Users/deniz/Desktop/Furh/furhat-dungeon-master/images/field_sitting.png").convert()
        self.furhat = furhat
        self.vahdet =  pygame.image.load("/Users/deniz/Desktop/Furh/furhat-dungeon-master/images/vahdet.png").convert()

    def get_words(self):
        counter = 0
        text = ""
        for word in self.words:
            text += " " 
            text += word
            counter += 1
            if counter == 5:
                text += "\n"
                counter = 0
        print(text)
        return text

    def ProcessInput(self, events, pressed_keys, game_params):
        pass

    def Update(self):
        self.furhat.say(self.text)

    def Render(self, WIN):
        self.slide += 0.3
        if self.slide > 200 and self.slide < 350:
            WIN.fill((240,240,240))
            WIN.blit(self.vahdet, (40,0+(self.slide/30)))
            
        elif self.slide > 700 and self.slide < 900:
            WIN.blit(self.school_photo, (0,0+(self.slide/60)))

        else:
            WIN.fill((20,20,30))
            
            for i,text in enumerate(self.rect_texts):
                text = self.font.render(text, True, (255 ,255 ,255))
                WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i)))