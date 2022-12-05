from .scene_base import SceneBase
import pygame

class FurhatPhotoScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.slide = 0
		self.furhat_img = pygame.image.load("furhat.jpeg").convert_alpha()

	
	def ProcessInput(self, events, pressed_keys):
		if pressed_keys[pygame.K_SPACE]:
			self.Terminate()
		
	def Update(self):
		print("update furhat")
	
	def Render(self, WIN):
		# The game scene is just a blank blue screen 
		self.slide += 0.1
		WIN.fill((255, 255, 255))
		WIN.blit(self.furhat_img, (0-self.slide,0))