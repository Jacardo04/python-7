from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.card = {}
        self.next_id = 1
        self.match_history = []

    def reg_card(self, card: TournamentCard) -> str:
        card_id = f"C{self.next_id}"
        self.cards[card_id] = card
        self.next_id += 1
        return card_id

    def creat_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_win(1)
        loser.update_losses(1)

        match_result = {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

        self.match_history.append(match_result)
        return match_result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.values(),
                              key=lambda c: c.calculate_rating(), reverse=True)
        return [{"name": c.name, "rating": c.calculate_rating()}
                for c in sorted_cards]

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.match_history),
            "leaderboard": self.get_leaderboard()
        }
