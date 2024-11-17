import pygame

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw(self, canvas):
        rect = pygame.Rect(50, 50,700,500)
        pygame.draw.rect(canvas, (100,0,0), rect)
        text = self.font.render(f'Game Over', True, (255,255,255))
        text_rect = pygame.Rect(300, 300 - 32/2,700,500)
        canvas.blit(text, text_rect)