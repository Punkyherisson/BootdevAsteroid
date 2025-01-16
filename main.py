# Import the pygame library
import pygame

# Import constants from constants.py
from constants import *

#Import the Player Class (sprite step)
from player import Player

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen with the defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Game")

     # Create a Clock object to manage FPS
    clock = pygame.time.Clock()
    dt=0
    
    # We create 2 groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Create a Player Instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add player to the group
    updatable.add(player)
    drawable.add(player)
 
    # Game loop
    running = True
    while running:
        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Fill the screen with a solid black color
        screen.fill((0, 0, 0))
        # Update all updatable entities
        for entity in updatable:
            entity.update(dt)
        # Draw all drawable entities
        for entity in drawable:
            entity.draw(screen)

        # Refresh the screen (update the display)
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000  # delta time in seconds

        #update the player rotation
        player.update(dt)   

    # Quit pygame when the game loop ends
    pygame.quit()

if __name__ == "__main__":
    main()