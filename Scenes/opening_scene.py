from .scene_base import SceneBase
import pygame
from Util.text_manup import wrapline
import CONSTANTS
class OpeningScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.next = self
        self.font = pygame.font.SysFont(None, 50)
        self.text = "This  tale  grew  in  the  telling,  until  it  became  a  history  of  the Great  War  of  the  Ring  and  included  many  glimpses  of  the yet  more  ancient  history  that  preceded  it.  It  was  begun  soon after  The  Hobbit  was  written  and  before  its  publication  in 1 937;  but  I  did  not  go  on  with  this  sequel,  for  I  wished  first to  complete  and  set  in  order  the  mythology  and  legends  of the  Elder  Days,  which  had  then  been  taking  shape  for  some years.  I  desired  to  do  this  for  my  own  satisfaction,  and  I  had little  hope  that  other  people  would  be  interested  in  this  work, especially  since  it  was  primarily  linguistic  in  inspiration  and was  begun  in  order  to  provide  the  necessary  background  of ‘history’  for  Elvish  tongues. When  those  whose  advice  and  opinion  I  sought  corrected little  hope  to  no  hope ,  I  went  back  to  the  sequel,  encouraged by  requests  from  readers  for  more  information  concerning hobbits  and  their  adventures.  But  the  story  was  drawn  irresistibly  towards  the  older  world,  and  became  an  account,  as it  were,  of  its  end  and  passing  away  before  its  beginning  and middle  had  been  told.  The  process  had  begun  in  the  writing of  The  Hobbit ,  in  which  there  were  already  some  references to  the  older  matter:  Elrond,  Gondolin,  the  High-elves,  and the  ores,  as  well  as  glimpses  that  had  arisen  unbidden  of things  higher  or  deeper  or  darker  than  its  surface:  Durin, Moria,  Gandalf,  the  Necromancer,  the  Ring.  The  discovery of  the  significance  of  these  glimpses  and  of  their  relation  to the  ancient  histories  revealed  the  Third  Age  and  its  culmination  in  the  War  of  the  Ring. Those  who  had  asked  for  more  information  about  hobbits eventually  got  it,  but  they  had  to  wait  a  long  time;  for  the composition  of  The  Lord  of  the  Rings  went  on  at  intervals during  the  years  1936  to  1949,  a  period  in  which  I  had  many duties  that  I  did  not  neglect,  and  many  other  interests  as  a learner  and  teacher  that  often  absorbed  me.  The  delay  was,"
        self.rect_texts = wrapline(self.text, self.font, CONSTANTS.WIDTH)
        self.slide = 0

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
        pass

    def Render(self, WIN):
        self.slide += 0.2
        WIN.fill((255,255,255))
        
        for i,text in enumerate(self.rect_texts):
            text = self.font.render(text, True, (0,0,0))
            WIN.blit(text, text.get_rect(topleft=(0, 0-self.slide + 35*i)))