import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(pygame.sprite.Sprite):
	def __init__(self, bullet_position, velocity):
		super().__init__()
		self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
		pygame.draw.circle(self.image, (255,255,255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS, 2)
		self.rect = self.image.get_rect(center=(bullet_position.x, bullet_position.y))
		self.velocity = velocity
		self.position = bullet_position
		self.radius = 5

	def update(self, dt):
		self.rect.centerx += self.velocity.x * dt
		self.rect.centery += self.velocity.y * dt
		self.position += self.velocity * dt

	def collision_check(self, target):
		distance_between_shapes = self.position.distance_to(target.position)
		if self.radius + target.radius >= distance_between_shapes:
			return True
		return False
