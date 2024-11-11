import pygame

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0,0,255), self.rect)

    def update(self, vx):
        self.x += vx
        self.rect.x = self.x