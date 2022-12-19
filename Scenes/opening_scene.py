from .scene_base import SceneBase
import pygame

class OpeningScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.next = self
        self.font = pygame.font.SysFont(None, 50)
        self.text = "This  tale  grew  in  the  telling,  until  it  became  a  history  of  the Great  War  of  the  Ring  and  included  many  glimpses  of  the yet  more  ancient  history  that  preceded  it.  It  was  begun  soon after  The  Hobbit  was  written  and  before  its  publication  in 1 937;  but  I  did  not  go  on  with  this  sequel,  for  I  wished  first to  complete  and  set  in  order  the  mythology  and  legends  of the  Elder  Days,  which  had  then  been  taking  shape  for  some years.  I  desired  to  do  this  for  my  own  satisfaction,  and  I  had little  hope  that  other  people  would  be  interested  in  this  work, especially  since  it  was  primarily  linguistic  in  inspiration  and was  begun  in  order  to  provide  the  necessary  background  of ‘history’  for  Elvish  tongues. When  those  whose  advice  and  opinion  I  sought  corrected little  hope  to  no  hope ,  I  went  back  to  the  sequel,  encouraged by  requests  from  readers  for  more  information  concerning hobbits  and  their  adventures.  But  the  story  was  drawn  irre¬ sistibly  towards  the  older  world,  and  became  an  account,  as it  were,  of  its  end  and  passing  away  before  its  beginning  and middle  had  been  told.  The  process  had  begun  in  the  writing of  The  Hobbit ,  in  which  there  were  already  some  references to  the  older  matter:  Elrond,  Gondolin,  the  High-elves,  and the  ores,  as  well  as  glimpses  that  had  arisen  unbidden  of things  higher  or  deeper  or  darker  than  its  surface:  Durin, Moria,  Gandalf,  the  Necromancer,  the  Ring.  The  discovery of  the  significance  of  these  glimpses  and  of  their  relation  to the  ancient  histories  revealed  the  Third  Age  and  its  culmi¬ nation  in  the  War  of  the  Ring. Those  who  had  asked  for  more  information  about  hobbits eventually  got  it,  but  they  had  to  wait  a  long  time;  for  the composition  of  The  Lord  of  the  Rings  went  on  at  intervals during  the  years  1936  to  1949,  a  period  in  which  I  had  many duties  that  I  did  not  neglect,  and  many  other  interests  as  a learner  and  teacher  that  often  absorbed  me.  The  delay  was,"
        self.words = self.text.split()
        self.rect_lines = []
    def ProcessInput(self, events, pressed_keys, game_params):
        pass

    def Update(self):
        pass

    def Render(self, WIN):
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 48)
        WIN.fill((255,255,255))
        current_line = []
        for word in self.words:
            pass