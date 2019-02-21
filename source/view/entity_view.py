from typing import Tuple

import pygame
from abc import ABC, abstractmethod

from pygame import Surface


class EntityView(ABC):
    """"
    Base class for all game entity's drawn.
    Every ViewEntity has a parent surface where it will be drawn on.
    Also every ViewEntity has a surface and can draw itself on a surface.
    """
    _parent_surface: Surface

    def __init__(self, parent_surface, pos, size):
        """
        :param parent_surface: The surface to draw on
        :param pos is a tuple (x,y)
        :param size is a tuple (width, height)
        """

        self._parent_surface = parent_surface
        self._pos = pos
        self._size = (round(size[0]), round(size[1]))

        self._surface = pygame.Surface(self._size)
        self._surface.fill((255, 255, 255))

        self._rect = self._surface.get_rect()
        self._rect.move_ip(self._pos[0], self._pos[1])

    @abstractmethod
    def _initialize_surface(self):
        """
        This function forces child classes to initialize the surface.
        Here so i don't forget to initialize the own surface in later classes
        """
        print("I shouldn't get called!")

    @property
    def rect(self):
        return self._rect

    def draw(self):
        """
        Function to draw an entity on his parent surface, Default behaviour just draw surface at pos surface.
        Can be overridden in.
        """

        assert self._surface is not None, "Child object has not defined surface, can't use default draw function of " \
                                          "entity "
        assert type(self._surface) == pygame.Surface, "Surface should be of type {0} not {1}" \
            .format(pygame.Surface, type(self._surface))
        self._parent_surface.blit(self._surface, self._pos)

    def clicked(self):
        """
        Function should be called when there is clicked on this view.
        Child classes should implement this function.
        This function handle's a click on a button.
        :return:
        """
        return self

    def _transform(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Transforms a previous coordinate so that the origin of the new coordinates
        are this surface
        :param pos: old coordinates
        :return: new coordinates
        """

        return pos[0] - self._pos[0], pos[1] - self._pos[1]
