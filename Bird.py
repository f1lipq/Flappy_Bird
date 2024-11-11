import pygame

class Bird:
	def __init__(self):
		self.y = 0
		self.vy = 0
		self.rect = pygame.Rect(80, 0,60,60)
		
	def fly_up(self):
		self.vy = -0.3
		
	def update(self):
		self.vy += 0.0005
		self.y += self.vy
		self.y = max(self.y, 0)
		self.rect.y = self.y
		#print(f'y: {self.y}, vy: {self.vy}')

	def draw(self, canvas):
		pygame.draw.rect(canvas, (255,0,0), self.rect)