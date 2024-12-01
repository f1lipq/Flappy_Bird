import pygame 
from pygame import mixer 
import random
from world.Bird import Bird
from world.Ground import Ground
from world.Track import Track
from screens.GameOverScreen import GameOverScreen

pygame.init() 
mixer.init() 

""" 
# Loading the song 
mixer.music.load("assets/videoGame.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  
# Start playing the song 
mixer.music.play() 
"""

canvas = pygame.display.set_mode((800,600)) 

pygame.display.set_caption("Bird") 

# states ---
PLAY_STATE = "play"
GAME_OVER_STATE = "game_over"
FOCUS_STATE = "focus"

#image = pygame.image.load("flappyBird.jpg") 
is_exit = False
game_state = FOCUS_STATE

track = Track()
bird = Bird()
game_over_screen = GameOverScreen()

fps = 60
clock = pygame.time.Clock()

"""
def end():
	game_over_screen.score = track.get_score()
	print(game_over_screen.score)
	saveBoolean =  str(input("Do you want to save? (y/n)"))
	if saveBoolean == 'y':
		username = str(input("Type your username: "))
		return username
	elif saveBoolean == 'n':
		return "Finished"
"""

def game_over():
	game_over_screen.score = track.get_score()
	print(f'Game over')
	print(f'Your score:{track.get_score()}')

def restart():
	print("Restart")
	bird.restart()
	track.restart()

font = pygame.font.Font('freesansbold.ttf', 32)

while not is_exit: 
	canvas.fill((255,255,255))
	mouse = pygame.mouse.get_pos()

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			is_exit = True
			print(f'Finished: {pygame.time.get_ticks()} ms')
			print(f'Your score:{track.get_score()}')
		if event.type == pygame.KEYDOWN and event.key == 32:
			if game_state == FOCUS_STATE:
				game_state = PLAY_STATE
			bird.fly_up()

		if game_state == GAME_OVER_STATE and event.type == pygame.MOUSEBUTTONDOWN:
			if game_over_screen.on_restart_click(mouse[0], mouse[1]) or event.type == pygame.K_RETURN:
				restart()
				game_state = FOCUS_STATE

		if event.type == pygame.KEYDOWN:
			if game_state == GAME_OVER_STATE and event.key == pygame.K_RETURN:
				restart()
				game_state = FOCUS_STATE

	if game_state == PLAY_STATE:
		bird.update()
		track.update()
		text = font.render(f'Your score: {track.get_score()}', True, (0,0,0), (255,255,255))
		canvas.blit(text, text.get_rect())

		if bird.rect.colliderect(track.ground.rect) or track.collide_bird(bird):
			game_over()
			game_state = GAME_OVER_STATE
	elif game_state == FOCUS_STATE:
		text = font.render(f'Press SPACE to start', True, (0,0,0), (255,255,255))
		canvas.blit(text, text.get_rect())

	track.draw(canvas)
	bird.draw(canvas)

	if game_state == GAME_OVER_STATE:
		game_over_screen.draw(canvas)

	#print(f'TOP: {block_height_top}, BOTTOM: {block_height_bottom}')
	pygame.display.update()
	clock.tick(fps)

#f = open("leaderboard.csv", "a")
#f.write(f'{end()},{points()},points\n')
#f.close