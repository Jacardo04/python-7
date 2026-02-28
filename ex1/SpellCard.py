from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    CARD_TYPE = "spell"

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("Must be Valid and not empty")

        self.effect_type = effect_type

    def play(self, game_state: Dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect_type": self.effect_type,
            "status": "Spell has been cast successfully"
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "resolution": "Effect has been resolved"
        }
