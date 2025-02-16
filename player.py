import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(),2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # left
            self.rotate(dt * -1)
        if keys[pygame.K_d]: # right
            self.rotate(dt)
        if keys[pygame.K_w]:  # forward
            self.move(dt)
        if keys[pygame.K_s]:  # backward
            self.move(dt * -1)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        