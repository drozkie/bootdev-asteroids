import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, BROWN, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vector = random.uniform(20, 50)

            new_velocity = self.velocity * ASTEROID_VELOCITY_MULTIPLIER

            asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

            asteroid1.velocity.rotate(vector)
            asteroid2.velocity.rotate(-vector)

            asteroid1.velocity += new_velocity
            asteroid2.velocity -= new_velocity