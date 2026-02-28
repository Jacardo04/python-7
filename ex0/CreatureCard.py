from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be greater or equal to 0.")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be greater or equal to 0.")

        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info.update({
         "type": self.type,
         "attack": self.attack,
         "health": self.health
        })
        return base_info

    def play(self, game_status: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to Playfield"
        }

    def attack_target(self, target) -> Dict:
        if not isinstance(target, CreatureCard):
            raise ValueError("You must taget a CreatureCard.")

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
