import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added.")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot draw from empty deck.")
        return self.cards.pop()

    def deck_size(self) -> int:
        return len(self.cards)

    def get_deck_stats(self) -> Dict:
        stats = {
            "total_cards": len(self.cards),
            "types": {}
        }

        for card in self.cards:
            card_type = type(card).__name__
            stats["types"][card_type] = stats["types"].get(card_type, 0) + 1

        return stats
