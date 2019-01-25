from abc import ABC, abstractmethod

from pygame import Surface


class EntityView(ABC):
    """"
    Base class for all game entity's drawn.
    Every ViewEntity has a parent surface where it will be drawn on.
    Also every ViewEntity has a surface and can draw itself on a surface.
    """
    _parent_surface: Surface

    def __init__(self, parent_surface):
        """
        :param parent_surface: The surface to draw on
        """

        self._parent_surface = parent_surface
        self._surface = None

    @abstractmethod
    def _initialize_surface(self):
        """
        This function forces child classes to initialize the surface.
        Here so i don't forget to initialize the own surface in later classes
        """
        print("I shouldn't get called!")

    def draw(self, x, y):
        """
        Function to draw an entity on his parent surface, Default behaviour just draw surface at pos surface.
        Can be overridden in.
        :param x:
        :param y:
        :return:
        """

        assert self._surface is not None, "Child object has not defined surface, can't use default draw function of " \
                                          "entity "

        self._parent_surface.blit(self._surface, (x, y))
