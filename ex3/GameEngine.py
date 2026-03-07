from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.playfield = []
        self.simed_turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        deck_data = factory.create_themed_deck(3)
        self.hand = deck_data["deck"]
        self.cards_created = len(self.hand)
