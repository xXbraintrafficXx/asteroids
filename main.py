# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init() 
	print("Starting asteroids!")
	
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	dps_clock = pygame.time.Clock()
	dt  = 0 #delta time

	#create and assign groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, drawable, updatable)

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y,PLAYER_RADIUS)
	asteroidfield = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0)) #rgb tuple for color, white would use 255
		
		for obj in drawable: #draw player & other objects in group
			obj.draw(screen) 
		for obj in updatable: #update player & other objects in group
			obj.update(dt)

		for obj in asteroids:
			if player.collides(obj): #asternoid kills player
				sys.exit("Game over!")
			for shot in shots:
				if shot.collides(obj): #player shot kills asteroid
					obj.kill()
					shot.kill()

		pygame.display.flip()

		 #set dps to reduce overloading resources, cpu was at 100% w/out
		dt = (dps_clock.tick(60) / 1000) 
		
	pygame.quit() 

if __name__ == "__main__":
	main()
