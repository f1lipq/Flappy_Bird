import pygame 
from pygame import mixer 
import random
from world.Bird import Bird
from world.Ground import Ground
from world.Track import Track
from screens.GameOverScreen import GameOverScreen

pygame.init() 
mixer.init() 
  
# Loading the song 
mixer.music.load("assets/videoGame.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  
# Start playing the song 
mixer.music.play() 

canvas = pygame.display.set_mode((800,600)) 

pygame.display.set_caption("Bird") 

#image = pygame.image.load("flappyBird.jpg") 
is_exit = False
is_game_over = False

track = Track()
bird = Bird()
ground = Ground()
game_over_screen = GameOverScreen()

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
			bird.fly_up()
		if is_game_over == True and event.type == pygame.MOUSEBUTTONDOWN:
			if game_over_screen.on_restart_click(mouse[0], mouse[1]):
				print("Restart")
				is_game_over = False
				bird.restart()
				track.restart()



	if is_game_over == False:
		bird.update()
		track.update()

		if bird.rect.colliderect(ground.rect) or track.collide_bird(bird):
			game_over()
			is_game_over = True

	ground.draw(canvas)
	bird.draw(canvas)
	track.draw(canvas)

	if is_game_over == True:
		game_over_screen.draw(canvas)

	text = font.render(f'Your score: {track.get_score()}', True, (0,0,0), (255,255,255))
	canvas.blit(text, text.get_rect())
	#print(f'TOP: {block_height_top}, BOTTOM: {block_height_bottom}')
	pygame.display.update() 

#f = open("leaderboard.csv", "a")
#f.write(f'{end()},{points()},points\n')
#f.close