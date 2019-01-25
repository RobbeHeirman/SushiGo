"""
:author Robbe Heirman
:Version 0.01

Will handle the position and viewing on the screen of a card class.s

Changelog:
    24/01/2019:
        * Added the CardView class
        * wrote static initializer to load all images into memory.
"""

import copy
import os

from pygame import Surface, image
import source.model.card as card
import source.view.entity_view as entity


class CardView(entity.EntityView):
    """ View for a card"""

    # Type suggestions of class members
    _model: card.Card

    # Class static block
    # ==================================================================================================================
    # the loaded image map
    IMAGE_DICT = dict()

    @staticmethod
    def init_card_view():
        """ Initializes the IMAGE_DICT by loading the images according to cardType"""

        base_path = os.path.join("../", "assets", "images")  # Path of images

        name_images = [
            (card.CardType.TEMPURA, "Tempura.png"),
            (card.CardType.MAKI_ROLLS, ["Maki_Roll1.png", "Maki_Roll2.png", "Maki_Roll3.png"]),
            (card.CardType.NIGIRI, ["Maki_Roll1.png", "Maki_Roll2.png", "Maki_Roll3.png"]),
            (card.CardType.Pudding, "Pudding.jpg"),
            (card.CardType.Wasabi, "Wasabi.jpg"),
            (card.CardType.Chopsticks, "Chopsticks.jpg")
        ]

        # Lazy coding loop to load all images in dict
        for type_enum, value in name_images:

            if type_enum == card.CardType.MAKI_ROLLS or type_enum == card.CardType.NIGIRI:

                # we make buckets for multi valued cards, (store it as a python list)
                CardView.IMAGE_DICT[type_enum] = list()
                for name in value:
                    CardView.IMAGE_DICT[type_enum].append(image.load(os.path.join(base_path, name)))

            else:
                CardView.IMAGE_DICT[type_enum] = image.load(os.path.join(base_path, value))

    # init block
    # ==================================================================================================================

    def __init__(self, parent_surface: Surface, model_card: card.Card):
        """
        :param parent_surface: Surface the card will be drawn on.
        :param model_card: The model this cardView belongs to.
        """

        super().__init__(parent_surface)

        # Assertion block
        assert type(parent_surface) == Surface, "Card parent surface should be {0} but is {1}" \
            .format(Surface, type(parent_surface))
        assert type(model_card) == card.Card, "Model of CardView should be of the type {0} and not {1}" \
            .format(card.Card, type(model_card))

        # Members
        self._model = model_card
        self._initialize_surface()

    def _initialize_surface(self):
        self._surface = copy.copy(CardView.IMAGE_DICT[self._model.type])

    # Properties
    # ==================================================================================================================

    @property
    def surface(self) -> Surface:
        return self._surface

    # Public functions
    # ==================================================================================================================

    def draw(self, x, y):
        self._parent_surface.blit(self._surface, x, y)


CardView.init_card_view()
