# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from player import Player


def main():
	pygame.init() 
	print("Starting asteroids!")
	
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	dps_clock = pygame.time.Clock()
	dt  = 0 #delta time


	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y,PLAYER_RADIUS)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0)) #rgb tuple for color, white would use 255
		player.draw(screen)

		pygame.display.flip()

		 #set dps to reduce overloading resources, cpu was at 100% w/out
		dt = (dps_clock.tick(60) / 1000) 
		#return dt
	pygame.quit() 

if __name__ == "__main__":
	main()
