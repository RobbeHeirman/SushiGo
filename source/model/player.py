from typing import List

from source.model.booster_pack import BoosterPack
from source.model.card import Card


class Player:
    _selected_cards: List[Card]
    _booster_pack: BoosterPack

    def __init__(self):
        self._selected_cards = []
        self._booster_pack = None

    @property
    def booster_pack(self):
        return self._booster_pack

    @booster_pack.setter
    def booster_pack(self, booster: BoosterPack):
        self._booster_pack = booster

    def pick_card(self, card):

        self._booster_pack.pick_card(card)
        self._selected_cards.append(card)
