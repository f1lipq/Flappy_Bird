import pygame 
from pygame import mixer 
import random
from world.Bird import Bird
from world.Ground import Ground
from world.Track import Track

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
exit = False

track = Track()
bird = Bird()
ground = Ground()

def points():
	time = pygame.time.get_ticks()
	points = 0
	points = time / 1000
	return int(points)

def end():
	saveBoolean =  str(input("Do you want to save? (y/n)"))
	if saveBoolean == 'y':
		username = str(input("Type your username: "))
		return username
	elif saveBoolean == 'n':
		return "Finished"

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'Your score: {points()}', True, (0,0,0), (255,255,255))
textRect = text.get_rect()

while not exit: 
	canvas.fill((255,255,255))
	canvas.blit(text, textRect)

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True
			print(f'Finished: {pygame.time.get_ticks()} ms')
			print(f'Your score:{points()}')
		if event.type == pygame.KEYDOWN and event.key == 32:
			bird.fly_up()

	bird.update()
	track.update()
	ground.draw(canvas)
	bird.draw(canvas)
	track.draw(canvas)

	if bird.rect.colliderect(ground.rect):
		print(f'Game over')
		print(f'Your score:{points()}')
		exit = True
	
	if track.collide_bird(bird):
		print("Game over")
		print(f'Your score:{points()}')
		exit = True
	
	text = font.render(f'Your score: {points()}', True, (0,0,0), (255,255,255))
	#print(f'TOP: {block_height_top}, BOTTOM: {block_height_bottom}')
	pygame.display.update() 

#f = open("leaderboard.txt.txt", "w")
#f.write(f'{end()}: {points()} points')
#f.close