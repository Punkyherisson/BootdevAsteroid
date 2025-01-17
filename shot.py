import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        # Move the shot in a straight line
        self.position += self.velocity * dt

    def draw(self, surface):
        # Draw the shot as a small circle
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius)