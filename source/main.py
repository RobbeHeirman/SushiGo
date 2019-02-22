"""
@Author: Robbe Heirman
@Version: 0.01

@Description:
Main python module for SushiGo!
Contains the GameLoop and event handler.
"""
import os
import sys
from typing import List, Tuple

import pygame

from source.model.deck import Deck
from source.model.player import Player
from source.view.entity_view import EntityView
from source.view.hand_view import HandView
from source.view.picked_cards_view import PickedCardsView

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


def is_clicked(views: List[EntityView], mouse_pos: Tuple[int, int]) -> EntityView:
    """
    Returns the view that is clicked in the game
    """

    for view in views:
        rct = view.rect
        if rct.collidepoint(mouse_pos):
            return view.clicked()


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
    player = Player()
    b_pack = deck.generate_booster(10)
    player.booster_pack = b_pack

    hand_view = HandView(screen, (0, SCREEN_HEIGHT - SCREEN_HEIGHT / 5), (SCREEN_WIDTH, SCREEN_HEIGHT / 5), player)
    pick_crds = PickedCardsView(screen, (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT / 5), player, 0)
    pick_crds2 = PickedCardsView(screen, (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT / 5), player, 180)
    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                is_clicked([hand_view, pick_crds, pick_crds2], pygame.mouse.get_pos())
        screen.fill((0, 0, 0))
        hand_view.draw()
        pick_crds.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
