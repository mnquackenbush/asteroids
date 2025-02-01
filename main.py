import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	AsteroidField.containers = (updatable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	Shot.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for object in asteroids:
			if object.collides(player) == True:
				print("Game over!")
				sys.exit()
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		ms_passed = clock.tick(60)
		dt = ms_passed / 1000

if __name__ == "__main__":
	main()
