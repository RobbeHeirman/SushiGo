"""
@Author: Robbe Heirman
@Version: 0.01

@Description:
Main python module for SushiGo!
Contains the GameLoop and event handler.
"""

import sys, pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    """
     Main function of our program.
    """

    # Initialization block
    pygame.init()  # Initialize pygame module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # initialize screen

    # Testing

    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
