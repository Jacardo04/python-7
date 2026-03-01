from ex3.GameStrategy import GameStrategy
from typing import List, Dict


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        played_cards = []
        for card in sorted(hand, key=lambda c: c.cost):
            played_cards.append(card.play({}))
        return {"strategy": self.get_strategy_name(),
                "played_cards": played_cards}

    def get_strategy_name(self) -> str:
        return "Aggressive"

    def prioritize_targets(self, available_targets: List) -> List:
        return sorted(available_targets, reverse=True)
