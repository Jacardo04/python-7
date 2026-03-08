from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.type = "Tournament"

    # Card method
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Card enters the tournament battlefield"
        }

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.health, incoming_damage // 2)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        return self.wins * 10 - self.losses * 5

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"wins": self.wins, "losses": self.losses,
                "rating": self.calculate_rating()}

    def get_tournament_stats(self) -> dict:
        return {
            **self.get_card_info(),
            **self.get_combat_stats(),
            **self.get_rank_info()
        }
