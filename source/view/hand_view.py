import pygame
import source.view.entity_view as entity_view


class HandView(entity_view.EntityView):
    """
    This is the surface all cards in hand will be on screen.
    This will be an invisible box that bounds the cards a player can choose from.
    The class should be a singleton on the UI. (could enforce this, but seems to off topic).
    The Surface for a hand is centered on the bottom of the screen (anchored).
     We could play around with the width and height
    """

    def _initialize_surface(self):

        # Creating an empty surface
        self._surface = pygame.Surface((self._width, self._height))
        self._surface.fill((255, 255, 255))

    def __init__(self, parent_surface, width, height):
        super().__init__(parent_surface)

        self._width = width
        self._height = height
        self._initialize_surface()

