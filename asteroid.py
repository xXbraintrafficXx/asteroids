import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #else split into smaller asteroids
        random_angle = random.uniform(20,50)
        self.radius -= ASTEROID_MIN_RADIUS
        #new-velocity = self.velocity

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        forward = self.velocity.rotate(random_angle)
        asteroid1.velocity = forward * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        forward = self.velocity.rotate(random_angle * -1)
        asteroid2.velocity = forward * 1.2


