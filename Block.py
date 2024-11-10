import pygame

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vx = -0.5
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0,0,255), self.rect)

    def update(self):
        self.x += self.vx
        self.rect.x = self.x
        #print(f'x: {self.x}, vx: {self.vx}, rect.x: {self.rect.x}')

    def comeback(self):
        self.x += 1730
        self.rect.x = self.x