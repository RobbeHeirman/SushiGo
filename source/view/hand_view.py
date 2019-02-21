from typing import List

import pygame

import source.view.entity_view as entity_view
from source.model.booster_pack import BoosterPack
from source.model.player import Player
from source.view.card_view import CardView


class HandView(entity_view.EntityView):
    """
    This is the surface all cards in hand will be on screen.
    This will be an invisible box that bounds the cards a player can choose from.
    The class should be a singleton on the UI. (could enforce this, but seems to off topic).
    The Surface for a hand is centered on the bottom of the screen (anchored).
     We could play around with the width and height
    """

    _player: Player
    _card_views: List[CardView]

    def _initialize_surface(self):
        # Creating an empty surface
        self._surface = pygame.Surface(self._size)
        self._surface.fill((255, 255, 255))

    def __init__(self, parent_surface, pos, size, player: Player):
        super().__init__(parent_surface, pos, size)

        self._initialize_surface()
        self._player = player
        self._card_views = []

    def draw(self):

        self._surface.fill((255, 255, 255))
        self._card_views = []
        for index, card in enumerate(self._player.booster_pack):
            card_width = self._size[0] / 10
            card_height = self._size[1]

            card_x = index * card_width
            card_y = 0

            card = CardView(self._surface, (card_x, card_y), (card_width, card_height), card)
            self._card_views.append(card)
            card.draw()

        super().draw()

    def clicked(self):

        transformed_pos = self._transform(pygame.mouse.get_pos())
        for card_view in self._card_views:
            if card_view.rect.collidepoint(transformed_pos):
                self._player.pick_card(card_view.model)
                return card_view

