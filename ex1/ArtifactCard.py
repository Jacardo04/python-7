from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    CARD_TYPE = "Artifact"

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)

        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must exist twin")

        if not isinstance(durability, int) or not durability:
            raise ValueError("durability must be above or equal to 0 twin")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect_type": self.durability,
            "status": "Artifact introduced to Playfield"
        }

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "status": "Artifact has withered to dust"
            }

        self.durability -= 1

        return {
             "artifact": self.name,
             "effect": self.effect,
             "remaining_durability": self.durability
            }
