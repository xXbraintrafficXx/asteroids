import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_cooldown = 0

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
        self.shot_cooldown -= dt

        if keys[pygame.K_a]: # left
            self.rotate(dt * -1)
        if keys[pygame.K_d]: # right
            self.rotate(dt)
        if keys[pygame.K_w]:  # forward
            self.move(dt)
        if keys[pygame.K_s]:  # backward
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:  # shoot
            self.shoot(dt)
            

    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shot_cooldown > 0:
            return
        else:    
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = direction * PLAYER_SHOOT_SPEED
        
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN