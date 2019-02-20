"""
@Author: Robbe Heirman
@Version: 0.01

@Description:
Main python module for SushiGo!
Contains the GameLoop and event handler.
"""
import os
import sys
from typing import List

import pygame

from source.model.deck import Deck
from source.view.entity_view import EntityView
from source.view.hand_view import HandView

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


def is_clicked(views: List[EntityView]) -> EntityView:
    """
    Returns the view that is clicked in the game
    """

    for view in views:
        rct = view.rect


def main():
    """
     Main function of our program.
    """

    # call to OS for positioning window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 25)

    # Initialization block
    pygame.init()  # Initialize pygame module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # initialize screen

    # Testing
    # model_card = m_card.Card(m_card.CardType.TEMPURA)
    # view_card = v_card.CardView(screen, model_card)

    deck = Deck()
    b_pack = deck.generate_booster(10)

    hand_view = HandView(screen,(0, SCREEN_HEIGHT - SCREEN_HEIGHT / 5), ( SCREEN_WIDTH, SCREEN_HEIGHT / 5), b_pack)
    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pass
        screen.fill((0, 0, 0))
        hand_view.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
