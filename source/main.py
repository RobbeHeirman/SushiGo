"""
@Author: Robbe Heirman
@Version: 0.01

@Description:
Main python module for SushiGo!
Contains the GameLoop and event handler.
"""
import os
import sys

import pygame

import source.model.card as m_card
from source.model.booster_pack import BoosterPack
from source.view.hand_view import HandView

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020


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

    card1 = m_card.Card(m_card.CardType.TEMPURA)
    card2 = m_card.Card(m_card.CardType.Pudding)
    b_pack = BoosterPack([card1, card2])
    hand_view = HandView(screen, SCREEN_WIDTH, SCREEN_HEIGHT / 5, b_pack)
    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        hand_view.draw(0, SCREEN_HEIGHT - SCREEN_HEIGHT / 5)
        pygame.display.flip()


if __name__ == "__main__":
    main()
