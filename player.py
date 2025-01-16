import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    #Call the parent class's constructor, also passing in PLAYER_RADIUS
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        #Create a field called rotation, initialized to 0
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # rotate left (counterclockwise)
            self.rotation -= PLAYER_TURN_SPEED * dt  # subtract to rotate left

        if keys[pygame.K_d]:  # rotate right (clockwise)
            self.rotation += PLAYER_TURN_SPEED * dt  # add to rotate right
    
    def update(self, dt):
        self.rotate(dt)  # Handle rotation based on user input