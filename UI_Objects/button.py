import pygame

# class Button():
# 	def __init__(self, x, y, image, scale):
# 		width = image.get_width()
# 		height = image.get_height()
# 		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
# 		self.rect = self.image.get_rect()
# 		self.rect.topleft = (x, y)
# 		self.clicked = False

# 	def draw(self, surface):
# 		action = False
# 		#get mouse position
# 		pos = pygame.mouse.get_pos()

# 		#check mouseover and clicked conditions
# 		if self.rect.collidepoint(pos):
# 			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
# 				self.clicked = True
# 				action = True

# 		if pygame.mouse.get_pressed()[0] == 0:
# 			self.clicked = False

# 		#draw button on screen
# 		surface.blit(self.image, (self.rect.x, self.rect.y))

# 		return action



class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)


	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)