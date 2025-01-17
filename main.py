# Import the pygame library
import pygame

# Import constants from constants.py
from constants import *
from shot import Shot
#Import the Player Class (sprite step)
from player import Player

from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen with the defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Game")

    # Create a Clock object to manage FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create a Player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Add player to the group
    updatable.add(player)
    drawable.add(player)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen
        screen.fill((0, 0, 0))

        # Update all entities
        for entity in updatable:
            entity.update(dt)

        # Check collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
                break

        # Check collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.kill()
                    shot.kill()

        # Draw all entities
        for entity in drawable:
            entity.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()