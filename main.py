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
    #Create a Player Instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create a Clock object to manage FPS
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Fill the screen with a solid black color
        screen.fill((0, 0, 0))
        
        # Render the Player in the Game Loop
        player.draw(screen)
        # Refresh the screen (update the display)
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000  # delta time in seconds

    # Quit pygame when the game loop ends
    pygame.quit()

if __name__ == "__main__":
    main()