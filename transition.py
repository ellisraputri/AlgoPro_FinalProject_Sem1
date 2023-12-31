import pygame

class Transition:
	def __init__(self, next_state, screen_width, screen_height):	
		self.display_surface = pygame.display.get_surface()
		self.next_state = next_state

		#overlay image
		self.image = pygame.Surface((screen_width,screen_height))
		self.color = 255
		self.speed = -2

	def play(self):
		#playing color transition
		self.color += self.speed
		if self.color <= 0:
			self.speed *= -1
			self.color = 0
			self.next_state()
		if self.color > 255:
			self.color = 255
			self.speed = -2

		self.image.fill((self.color,self.color,self.color))
		self.display_surface.blit(self.image, (0,0), special_flags = pygame.BLEND_RGBA_MULT)