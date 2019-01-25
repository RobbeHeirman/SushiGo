from typing import List

import pygame

import source.view.entity_view as entity_view
from source.model.booster_pack import BoosterPack
from source.view.card_view import CardView


class HandView(entity_view.EntityView):
    """
    This is the surface all cards in hand will be on screen.
    This will be an invisible box that bounds the cards a player can choose from.
    The class should be a singleton on the UI. (could enforce this, but seems to off topic).
    The Surface for a hand is centered on the bottom of the screen (anchored).
     We could play around with the width and height
    """
    _card_views: List[CardView]

    def _initialize_surface(self):
        # Creating an empty surface
        self._surface = pygame.Surface((self._width, self._height))
        self._surface.fill((255, 255, 255))

    def __init__(self, parent_surface, width, height, booster_pack: BoosterPack = None):
        super().__init__(parent_surface)

        self._width = width
        self._height = height
        self._initialize_surface()
        self._booster_pack = booster_pack

        self._card_views = list()
        for card in self._booster_pack:
            card_width = self._width / 10
            card_height = self._height

            card_view = CardView(self._surface, card, card_width, card_height)
            self._card_views.append(card_view)

    def draw(self, x, y):

        for index, card in enumerate(self._card_views):
            card_x = index * card.width
            card_y = 0
            card.draw(card_x, card_y)

        super().draw(x, y)
