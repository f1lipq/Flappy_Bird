import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ground:
	def __init__(self):
		self.height = 100
		self.rect = pygame.Rect(0, SCREEN_HEIGHT - self.height, SCREEN_WIDTH, self.height)

	def draw(self, canvas):
		pygame.draw.rect(canvas, (0,150,0), self.rect)