import pygame
import random
from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)


	def update(self, dt):
		self.position += (self.velocity * dt)


	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			vector_one = self.velocity.rotate(random_angle)
			vector_two = self.velocity.rotate(-random_angle)
			new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_one = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
			asteroid_one.velocity = vector_one * 1.2
			asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
			asteroid_two.velocity = vector_two * 1.2
			return asteroid_one, asteroid_two
