"""
:author Robbe Heirman
:Version 0.01

Will handle the position and viewing on the screen of a card class.s

Changelog:
    24/01/2019:
        * Added the CardView class
        * start writing static initalizer to load all images into memory.

    # TEMPURA = 0
    #SASHIMI = 1
    #MAKI_ROLLS = 2
    #NIGIRI = 3
    #EGG_NIGIRI = 4
    #Pudding = 5
    #Wasabi = 6
    #Chopsticks = 7
"""

import os, copy
import source.model.card as card
from pygame import Surface


class CardView:
    """ View for a card"""

    # Class static block
    # ==================================================================================================================
    # the loaded image map
    IMAGE_DICT = dict()

    @staticmethod
    def init_card_view():
        """ Initializes the IMAGE_DICT by loading the images according to cardType"""

        base_path = os.path.join("../", "assets", "images")  # Path of images
        CardView.IMAGE_DICT[card.CardType.TEMPURA] = os.path.join(base_path, "Tempura.png")
        # TODO: Add all other images after this works

    # init block
    # ==================================================================================================================

    def __init__(self, parent_surface: Surface, model_card: card.Card):
        """
        :param parent_surface: Surface the card will be drawn on.
        :param model_card: The model this cardView belongs to.
        """

        # Assertion block
        assert type(parent_surface) == Surface, "Card parent surface should be {0} but is {1}"\
            .format(Surface, type(parent_surface))
        assert type(model_card) == card.Card, "Model of CardView should be of the type {0} and not {1}"\
            .format(card.Card, type(model_card))

        # Members
        self._parent_surface = parent_surface
        self._model = model_card
        self._surface = CardView.IMAGE_DICT[self._model.type]

    # Properties
    # ==================================================================================================================

    @property
    def surface(self):
        return self._surface


CardView.init_card_view()
