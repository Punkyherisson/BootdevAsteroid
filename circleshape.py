import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collides_with(self, other):
        """
        Check if this CircleShape collides with another CircleShape.
        :param other: The other CircleShape object to check collision against.
        :return: True if the shapes collide, False otherwise.
        """
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
    def wrap_around_screen(self):
        # Wrap position to the other side if it goes out of bounds
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
