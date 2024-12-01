import pygame

class GameOverScreen:
    def __init__(self):
        self.game_over_font = pygame.font.Font('assets/game_over_font.ttf', 50)
        self.other_font = pygame.font.Font('assets/game_over_font.ttf', 30)
        self.score = 0
        self.rect_restart_button = pygame.Rect(280, 460,240,60)

    def draw(self, canvas):
        rect = pygame.Rect(250, 150,300,400)
        pygame.draw.rect(canvas, (72, 60, 50), rect, border_radius = 20)
        text = self.game_over_font.render(f'Game Over', True, (74, 4, 4))
        text_rect = text.get_rect()
        text_rect.center = (400, 80)
        #text_rect = pygame.Rect(300, 100 - 32/2,700,500)
        score_text = self.other_font.render(f'Your score: {self.score}', True, (255,255,255))
        score_rect = score_text.get_rect()
        score_rect.center = (400, 420)
        #score_rect = pygame.Rect(290, 200 - 32/2,700,500)
        canvas.blit(text, text_rect)
        canvas.blit(score_text, score_rect)

        # button ---
        pygame.draw.rect(canvas, (255,255,255), self.rect_restart_button, border_radius = 25)
        restart_text = self.other_font.render(f'Try again', True, (0,0,0))
        restart_rect = restart_text.get_rect()
        restart_rect.center = (400, 490)
        canvas.blit(restart_text, restart_rect)

        # leaderboard ---
        leaderboard_text = self.other_font.render(f'Leaderboard: ', True, (255,255,255))
        leaderboard_rect = leaderboard_text.get_rect()
        leaderboard_rect.center = (400, 200)
        canvas.blit(leaderboard_text, leaderboard_rect)

    def on_restart_click(self, x, y):
        if self.rect_restart_button.collidepoint(x, y):
            return True