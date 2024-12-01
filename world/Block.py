import pygame

class Block:
    def __init__(self, x, y, width, height, is_top):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_top = is_top
        
        if is_top:
            self.rect = pygame.Rect(self.x, -400 + self.height, self.width, 400)
        else:
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.top_block_img = pygame.image.load("assets\\top_pipe.png")
        self.bottom_block_img = pygame.image.load("assets\\bottom_pipe.png")

    def draw(self, canvas):
        if self.is_top:
            canvas.blit(self.top_block_img, self.rect)
        else:
            canvas.blit(self.bottom_block_img, self.rect)

    def update(self, vx):
        self.x += vx
        self.rect.x = self.x