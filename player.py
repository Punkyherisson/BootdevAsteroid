import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    #Call the parent class's constructor, also passing in PLAYER_RADIUS
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        #Create a field called rotation, initialized to 0
        self.rotation = 0
        self.shoot_timer = 0  # Timer for shooting

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.shoot_timer <= 0:  # Only allow shooting if timer is 0 or less
            # Create a shot at the player's current position
            forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction the player is facing
            velocity = forward * PLAYER_SHOOT_SPEED  # Scale the direction vector
            Shot(self.position.x, self.position.y, velocity)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
 
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Vector pointing in the direction of the ship
        self.position += forward * PLAYER_SPEED * dt          # Move forward/backward based on speed and dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Handle rotation
        if keys[pygame.K_LEFT]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:  # Rotate right
            self.rotate(dt)

        # Handle movement
        if keys[pygame.K_UP]:  # Move forward
            self.move(dt)
        if keys[pygame.K_DOWN]:  # Move backward
            self.move(-dt)  # Negative dt to move backward

        # Handle shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease the shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        super().update(dt)

