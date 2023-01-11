from .scene_base import SceneBase
from Scenes.volunteer_scene import VolunteerScene
import pygame
from Util.text_manup import wrapline
import CONSTANTS
from .game_story import story, story2, story3, story4, full_text
import os
    
class OpeningScene(SceneBase):
    def __init__(self, furhat):
        SceneBase.__init__(self)
        self.images_folder = os.path.join(os.getcwd(), "images")
        self.fonts_folder = os.path.join(os.getcwd(), "fonts")
        self.next = self
        self.font = pygame.font.Font(os.path.join(self.fonts_folder,"starjedi.ttf"), 50)
        self.text = full_text
        self.rect_texts = wrapline(self.text, self.font, CONSTANTS.WIDTH)
        self.story_rects = wrapline(story, self.font, CONSTANTS.WIDTH)
        self.story2_rects = wrapline(story2, self.font, CONSTANTS.WIDTH)
        self.story3_rects = wrapline(story3, self.font, CONSTANTS.WIDTH)
        self.story4_rects = wrapline(story4, self.font, CONSTANTS.WIDTH)
        self.slide = 0
        self.school_photo = pygame.image.load(os.path.join(self.images_folder, "field_sitting.png")).convert()

        self.furhat = furhat
        self.vahdet =  pygame.image.load(os.path.join(self.images_folder, "vahdet.png")).convert()

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
        self.furhat.look_at_other_player()
        self.furhat.say(story)
        self.furhat.look_at_other_player()
        self.furhat.say(story2)
        self.furhat.look_at_other_player()
        self.furhat.say(story3)
        self.furhat.look_at_other_player()
        self.furhat.say(story4)

        self.SwitchToScene(VolunteerScene(self.furhat))

    def Render(self, WIN):
        self.slide += 0.25
        if self.slide > 200 and self.slide < 350:
            WIN.fill((240,240,240))
            WIN.blit(self.vahdet, (40,0+(self.slide/30)))
            
        elif self.slide > 700 and self.slide < 900:
            WIN.blit(self.school_photo, (0,0+(self.slide/60)))

        else:
            WIN.fill((20,20,30))
            # for i,text in enumerate(self.rect_texts):
            #     text = self.font.render(text, True, (255 ,255 ,255))
            #     WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i)))

            for i,text in enumerate(self.story_rects):
                text = self.font.render(text, True, (255 ,255 ,255))
                WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i)))
            for i,text in enumerate(self.story2_rects):
                text = self.font.render(text, True, (255 ,255 ,255))
                WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i + 600)))
            for i,text in enumerate(self.story3_rects):
                text = self.font.render(text, True, (255 ,255 ,255))
                WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i + 1100)))
            for i,text in enumerate(self.story4_rects):
                text = self.font.render(text, True, (255 ,255 ,255))
                WIN.blit(text, text.get_rect(topleft=(5, 0-self.slide + 50*i + 1600)))
