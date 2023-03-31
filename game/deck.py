import random
from typing import List, Tuple
from .card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(number=i) for i in range(1, 53)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def split_into_half(self) -> Tuple[List[Card], List[Card]]:
        return self.cards[:26], self.cards[26:]
