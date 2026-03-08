from ex3.GameStrategy import GameStrategy
from typing import List, Dict


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> Dict:
        played_cards = []
        mana_used = 0
        targets_attacked = []
        total_damage = 0

        available_mana = 10  # you can adjust per your game logic
        for card in sorted(hand, key=lambda c: c.cost):
            if card.is_playable(available_mana):
                result = card.play({})
                played_cards.append(result)
                mana_used += card.cost

                if hasattr(card, "attack") or hasattr(card, "attack_power"):
                    damage = getattr(card, "attack_power", 0)
                    total_damage += damage
                    targets_attacked.append("Enemy Player")

                available_mana -= card.cost

        return {
            "cards_played": [c["card_played"] for c in played_cards],
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": total_damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return sorted(available_targets, reverse=True)
