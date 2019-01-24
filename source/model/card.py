"""

@author: Robbe Heirman
@version: 0.01

@Description
The model Card Class for the sushiGo Game.
SushiGo! is a game containing the following cards.
This class will contain all the logic of holding and handling a card.

Basic Game:
   Tempura
   Sashimi
   Dumpling
   1 Maki rolls
   2 Maki rolls
   3 Maki rolls
   Salmon Nigiri
   Squid Nigiri
   Egg Nigiri
   Pudding
   Wasabi
   Chopsticks

Changelog:

0.01 Date: 24/01/2019
Set up enumerator to differentiate between cards.

"""

import enum


class CardType(enum.Enum):
    """Enumerator to differentiate between CardTypes"""
    TEMPURA = 0
    SASHIMI = 1
    MAKI_ROLLS = 2
    NIGIRI = 3
    EGG_NIGIRI = 4
    Pudding = 5
    Wasabi = 6
    Chopsticks = 7


class Card:
    """"
    Card class of the SushiGo game. Each card in the game will be an instance of "Card" or from a derived
    class of Card.
    """

    _TYPE: CardType

    def __init_(self, card_type: CardType):
        """
        A card is always of a certain type
        :arg card_type = a CardType that is the type of the card instance
        """

        assert type(card_type) == CardType, "CardType should be {0}, not {1}".format(CardType, type(card_type))

        self._TYPE = card_type

    @property
    def type(self):
        """ Type is a constant."""
        return self._TYPE


class ValuedCard(Card):
    """
    Cards like "Nigiri" and "Maki Roll" have cards that are considered the same type of card but with
    different values. They are handled the same when scores are calculated but some are worth more/less
    based on their value (see game rules).
    """

    _VALUE: int

    def __init__(self, card_type: CardType, value: int):
        """Constructor"""

        super().__init__(card_type)

        # Assertion block
        assert type(value) == int, "ValuedCards should get an integer, not {0}".format(type(value))

        self._VALUE = value

    @property
    def value(self):
        """ Value is a constant"""
        return self._VALUE
