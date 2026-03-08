from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.next_id = 1
        self.match_history = []

    def reg_card(self, card: TournamentCard) -> str:
        card_id = f"C{self.next_id}"
        card.card_id = card_id
        self.cards[card_id] = card
        self.next_id += 1
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        match_result = {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

        self.match_history.append(match_result)
        return match_result

    def get_leaderboard(self):
        """Return cards sorted by rating descending"""
        cards_list = list(self.cards.values())
        """ simple bubble-sort style sort by rating"""
        for i in range(len(cards_list)):
            for j in range(i+1, len(cards_list)):
                if (cards_list[j].calculate_rating() >
                        cards_list[i].calculate_rating()):
                    temp = cards_list[i]
                    cards_list[i] = cards_list[j]
                    cards_list[j] = temp

        leaderboard = []
        for c in cards_list:
            leaderboard.append({
                "name": c.name,
                "rating": c.calculate_rating(),
                "wins": c.wins,
                "losses": c.losses
            })
        return leaderboard

    def generate_tournament_report(self):
        """Summary of tournament"""
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.match_history),
            "avg_rating":
            sum(c.calculate_rating() for c in self.cards.values()) //
            len(self.cards),
            "platform_status": "active"
        }
