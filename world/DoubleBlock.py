import pygame
from .Block import Block

class DoubleBlock:
    def __init__(self, x1, y1, width1, height1, x2, y2, width2, height2):
        self.top_block = Block(x1, y1, width1, height1, True)
        self.bottom_block = Block(x2, y2, width2, height2, False)

    def update(self, vx):
        self.top_block.update(vx)
        self.bottom_block.update(vx)

    def draw(self, canvas):
        self.top_block.draw(canvas)
        self.bottom_block.draw(canvas)

    def collide_bird(self, bird):
        if bird.rect.colliderect(self.top_block.rect) or bird.rect.colliderect(self.bottom_block.rect):
            return True
        return False