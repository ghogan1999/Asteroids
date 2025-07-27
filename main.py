import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	shots = pygame.sprite.Group()
	Shot.containers = shots

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots, 0)

	updatable.add(player)
	drawable.add(player)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black", rect=None, special_flags=0)
		for drawables in drawable:
			drawables.draw(screen)
		updatable.update(dt)
		shots.update(dt)
		shots.draw(screen)
		pygame.display.update()
		for asteroid in asteroids:
			if player.collision_check(asteroid) == True:
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for bullet in shots:
				if bullet.collision_check(asteroid):
					bullet.kill()
					result = asteroid.split()
					if result:
						for new_asteroid in result:
							asteroids.add(new_asteroid)
		dt = clock.tick(60) / 1000

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
