import pygame

class GameOverScreen:
    def __init__(self):
        self.game_over_font = pygame.font.Font('assets/game_over_font.ttf', 50)
        self.other_font = pygame.font.Font('assets/game_over_font.ttf', 30)
        self.f = open("bestScore.csv", "r")
        self.score = 0
        self.best = 0
        self.rect = pygame.Rect(250, 150,300,150)
        self.rect_restart_button = pygame.Rect(280, 350,240,60)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (72, 60, 50), self.rect, border_radius = 20)
        text = self.game_over_font.render(f'Game Over', True, (74, 4, 4))
        text_rect = text.get_rect()
        text_rect.center = (400, 80)
        canvas.blit(text, text_rect)

        # button ---
        pygame.draw.rect(canvas, (255,255,255), self.rect_restart_button, border_radius = 25)
        restart_text = self.other_font.render(f'Try again', True, (0,0,0))
        restart_rect = restart_text.get_rect()
        restart_rect.center = (400, 380)
        canvas.blit(restart_text, restart_rect)

        # Best, Score ---
        Scores_text = self.other_font.render(f'Score:   Best:', True, (255,255,255))
        Scores_rect = Scores_text.get_rect()
        Scores_rect.center = (400, 200)
        canvas.blit(Scores_text, Scores_rect)

        # Scores in numbers ---
        score_text = self.other_font.render(f'{self.score}        {self.best}', True, (255,255,255))
        score_rect = score_text.get_rect()
        score_rect.center = (400, 250)
        canvas.blit(score_text, score_rect)

    def on_restart_click(self, x, y):
        if self.rect_restart_button.collidepoint(x, y):
            return True