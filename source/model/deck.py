from source.model.booster_pack import BoosterPack
from source.model.card import CardType, Card, ValuedCard
import random


class Deck:
    """
    Class that represents a deck.
    Can draw booster packs and initialize a deck bases on the cards that should be in

    """
    CONFIG_DICT = {
        CardType.TEMPURA: 14,
        CardType.SASHIMI: 14,
        CardType.DUMPLING: 14,
        CardType.MAKI_ROLLS: [6, 12, 8],  # 1, 2 and 3 maki roll in order
        CardType.NIGIRI: [5, 10, 5],  # egg salmon and squid nigiri in order
        CardType.PUDDING: 10,
        CardType.WASABI: 6,
        CardType.CHOPSTICKS: 4
    }

    def __init__(self):
        self._deck_container = []  # Contains all the cards

        for card_type, amount in Deck.CONFIG_DICT.items():

            if card_type == CardType.MAKI_ROLLS or card_type == CardType.NIGIRI:

                for index, i in enumerate(amount):
                    self._deck_container += i * [ValuedCard(card_type, index)]

            else:
                self._deck_container += amount * [Card(card_type)]

        self.shuffle()

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self._deck_container)

    def generate_booster(self, size: int) -> BoosterPack:
        """Generates a booster from deck. This removes the cards from the deck and puts them in the booster."""

        drawn_cards = [self._deck_container.pop() for _ in range(0, size)]
        ret_pack = BoosterPack(drawn_cards)
        return ret_pack
