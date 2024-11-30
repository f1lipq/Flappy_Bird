import pygame

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = 0
        self.rect_restart_button = pygame.Rect(280, 350,200,80)

    def draw(self, canvas):
        rect = pygame.Rect(50, 50,700,500)
        pygame.draw.rect(canvas, (100,0,0), rect)
        text = self.font.render(f'Game Over', True, (255,255,255))
        score_text = self.font.render(f'Your score: {self.score}', True, (255,255,255))
        text_rect = pygame.Rect(300, 100 - 32/2,700,500)
        score_rect = pygame.Rect(290, 200 - 32/2,700,500)
        canvas.blit(text, text_rect)
        canvas.blit(score_text, score_rect)

        # button ---
        pygame.draw.rect(canvas, (255,255,255), self.rect_restart_button, border_radius = 25)
        restart_text = self.font.render(f'Try again', True, (0,0,0))
        restart_rect = pygame.Rect(300, 350 + 32/2,700,500)
        canvas.blit(restart_text, restart_rect)

    def on_restart_click(self, x, y):
        if self.rect_restart_button.collidepoint(x, y):
            return True