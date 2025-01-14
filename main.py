# Import the pygame library
import pygame

# Import constants from constants.py
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen with the defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    running = True
    while running:
        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Fill the screen with a solid black color
        screen.fill((0, 0, 0))

        # Refresh the screen (update the display)
        pygame.display.flip()

    # Quit pygame when the game loop ends
    pygame.quit()

if __name__ == "__main__":
    main()