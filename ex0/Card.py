from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if not isinstance(name, str) or not name:
            raise ValueError("Card name must exist cannot be empty.")

        if not isinstance(name, str) or not name:
            raise ValueError("Card cannot have negative cost.")

        if not isinstance(rarity, str) or not rarity:
            raise ValueError("card must have a valid rarity type")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """ability to play the game"""
        pass

    def get_card_info(self) -> Dict:
        """gives us the card info when called"""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """checks if u have enough mana to play the card"""
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError("MANA can never be negative")
        return available_mana >= self.cost
