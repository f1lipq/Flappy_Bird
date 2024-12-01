import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ground:
	def __init__(self):
		self.height = 100
		self.x = 0
		self.background_x = 0
		self.rect = pygame.Rect(0, SCREEN_HEIGHT - self.height, SCREEN_WIDTH, self.height)
		self.ground_img = pygame.image.load("assets/ground.png")
		self.background_img = pygame.image.load("assets/background.png")

	def draw_ground(self, canvas):
		#pygame.draw.rect(canvas, (0,150,0), self.rect)
		canvas.blit(self.ground_img, (self.x,SCREEN_HEIGHT - self.height))
		canvas.blit(self.ground_img, (SCREEN_WIDTH + self.x,SCREEN_HEIGHT - self.height))

	def draw_background(self, canvas):
		canvas.blit(self.background_img, (self.background_x, 0))
		canvas.blit(self.background_img, (SCREEN_WIDTH + self.background_x, 0))

	def update(self, x):
		self.x = x
		while self.x < - 800:
			self.x += 800

		self.background_x -= 0.5
		while self.background_x < - 800:
			self.x += 800