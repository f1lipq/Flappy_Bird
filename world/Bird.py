import pygame

class Bird:
	def __init__(self):
		self.restart()
		self.flappyBird_img = pygame.image.load("assets\\flappyBird.png")
		
	def fly_up(self):
		self.vy = -7
		self.rotate_angle = 30
		
	def update(self):
		self.vy += 0.3
		self.y += self.vy
		self.y = max(self.y, 0)
		self.rect.y = self.y
		if self.rotate_angle >= -80:
			self.rotate_angle -= 1
		#print(f'y: {self.y}, vy: {self.vy}')

	def draw(self, canvas):
		#pygame.draw.rect(canvas, (255,0,0), self.rect)
		rotate_bird = pygame.transform.rotate(self.flappyBird_img, self.rotate_angle)
		canvas.blit(rotate_bird, self.rect)

	def restart(self):
		self.rotate_angle = 0
		self.y = 200
		self.vy = 0
		self.rect = pygame.Rect(80, self.y,60,60)