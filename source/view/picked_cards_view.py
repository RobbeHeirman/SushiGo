from math import cos, sin, pi
from math import radians

import pygame
from pygame import Surface

from source.model.player import Player
from source.view.entity_view import EntityView


class PickedCardsView(EntityView):

    _rotation: int
    _player: Player

    def __init__(self, parent_surface, pos, size, player: Player, rotation: int = 0):
        """
        initalizer.
        :param parent_surface: see EntityView
        :param pos: see EntityView
        :param size: see EntityView
        :param player: the player who's picked cards those are
        :param rotation: rotation of the field.
        """

        super().__init__(parent_surface, pos, size)
        self._player = player
        self._rotation = rotation
        self._initialize_surface()

    def _initialize_surface(self):

        screen_width = self._parent_surface.get_width()
        screen_height = self._parent_surface.get_height()

        # We will place the drafted cards following a circle.
        # Transforming the designated boxes x_w, y_w and rotating them for each player
        x_w = screen_width / 5
        y_w = screen_height / 5



        print(y_w)
        # Center of screen
        x_c = screen_width / 2
        y_c = screen_height / 2 - screen_height / 10

        x_surface = round(x_c + (x_w * cos(radians(self._rotation - 90))))
        y_surface = round(y_c - (y_w * sin(radians(self._rotation - 90))))

        print(y_c)
        print(sin(radians(self._rotation )- pi/2))
        print(y_surface)

        surface_width = screen_width / 2
        x_surface -= surface_width / 2
        self._pos = (x_surface, y_surface)
        surface_height = screen_height / 6
        self._size = (surface_width, surface_height)
        self._surface = Surface(self._size)
        self._surface = pygame.transform.rotate(self._surface, self._rotation)
        self._surface.fill((255, 255, 255))

