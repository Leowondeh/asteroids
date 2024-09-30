import pygame, random
from constants import *
from sprites.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        spawnAngle = random.uniform(20, 50)
        resultAsteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        resultAsteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        resultAsteroid1.velocity = self.velocity.rotate(spawnAngle) * 1.2
        resultAsteroid2.velocity = self.velocity.rotate(-spawnAngle) * 1.2

        