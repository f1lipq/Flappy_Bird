import pygame
import random
from .DoubleBlock import DoubleBlock
from .Ground import Ground

class Track:
    def __init__(self):
        self.restart()

    def draw(self, canvas):
        self.ground.draw_background(canvas)
        self.block.draw(canvas)
        self.ground.draw_ground(canvas)

    def update(self):
        self.vx -= 0.005
        self.x += self.vx
        self.block.update(self.vx)
        self.ground.update(self.x)
        if self.block.top_block.x <= -70:
            if self.lower_rand <= 200 and self.higher_rand <= 250:
                self.lower_rand += 5
                self.higher_rand += 5
            self.block_height_top = random.randint(self.lower_rand, self.higher_rand)
            self.block_height_bottom = random.randint(self.lower_rand, self.higher_rand)
            self.block = DoubleBlock(1730, 0, 70, self.block_height_top, 1730, 500 - self.block_height_bottom, 70, self.block_height_bottom)

    def collide_bird(self, bird):
        return self.block.collide_bird(bird)
    
    def get_score(self):
        points = 0
        points = -self.x / 500
        return int(points)
    
    def restart(self):
        self.ground = Ground()
        self.x = 0
        self.vx = -11
        self.lower_rand = 50
        self.higher_rand = 150
        self.block_height_top = random.randint(self.lower_rand, self.higher_rand)
        self.block_height_bottom = random.randint(self.lower_rand, self.higher_rand)
        self.block = DoubleBlock(1730, 0, 70, self.block_height_top, 1730, 500 - self.block_height_bottom, 70, self.block_height_bottom)