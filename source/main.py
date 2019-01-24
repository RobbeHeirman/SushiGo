"""
@Author: Robbe Heirman
@Version: 0.01

@Description:
Main python module for SushiGo!
Contains the GameLoop and event handler.
"""

import sys, pygame
import source.model.card as m_card
import source.view.card_view as v_card

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
    model_card = m_card.Card(m_card.CardType.TEMPURA)
    view_card = v_card.CardView(screen, model_card)
    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(view_card.surface, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
