import pygame
import random
from DoubleBlock import DoubleBlock

class Track:
    def __init__(self):
        self.vx = -0.4
        self.lower_rand = 50
        self.higher_rand = 150
        self.block_height_top = random.randint(self.lower_rand, self.higher_rand)
        self.block_height_bottom = random.randint(self.lower_rand, self.higher_rand)
        self.block = DoubleBlock(1730, 0, 70, self.block_height_top, 1730, 500 - self.block_height_bottom, 70, self.block_height_bottom)

    def draw(self, canvas):
        self.block.draw(canvas)

    def update(self):
        self.vx -= 0.000005
        self.block.update(self.vx)
        if self.block.top_block.x <= -70:
            if self.lower_rand <= 200 and self.higher_rand <= 250:
                self.lower_rand += 5
                self.higher_rand += 5
            self.block_height_top = random.randint(self.lower_rand, self.higher_rand)
            self.block_height_bottom = random.randint(self.lower_rand, self.higher_rand)
            self.block = DoubleBlock(1730, 0, 70, self.block_height_top, 1730, 500 - self.block_height_bottom, 70, self.block_height_bottom)

    def collide_bird(self, bird):
        return self.block.collide_bird(bird)
        
