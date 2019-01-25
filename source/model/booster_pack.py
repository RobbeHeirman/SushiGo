from typing import List

from source.model.card import Card


class BoosterPack:
    """
    Model that represents a booster pack.
    a booster is a collection of SushiGo! cards passed around..
    """
    _card_container: List[Card]

    def __init__(self, cards: List[Card]):
        self._card_container = cards

    def __iter__(self):
        return iter(self._card_container)

    def __getitem__(self, item):
        return self._card_container
