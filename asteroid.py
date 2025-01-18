import pygame
from circleshape import CircleShape  # Assuming CircleShape is in circles.py
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius,velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity      

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_around_screen()

    def split(self):
        # 1. Kill the current asteroid
        self.kill()

        # 2. Check if the asteroid is small enough to not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid disappears

        # 3. Compute the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 4. Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # 5. Create two new velocity vectors for the smaller asteroids
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # 6. Spawn two new asteroids at the current position
        Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2)
   