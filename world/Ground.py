import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ground:
	def __init__(self):
		self.height = 100
		self.rect = pygame.Rect(0, SCREEN_HEIGHT - self.height, SCREEN_WIDTH, self.height)
		self.ground_img = pygame.image.load("assets\\ground.png")
		self.background_img = pygame.image.load("assets\\background.png")

	def draw_ground(self, canvas):
		#pygame.draw.rect(canvas, (0,150,0), self.rect)
		canvas.blit(self.ground_img, (0,SCREEN_HEIGHT - self.height))

	def draw_background(self, canvas):
		canvas.blit(self.background_img, (0,0))