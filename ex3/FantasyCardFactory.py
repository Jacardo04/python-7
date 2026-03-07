from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(["Dragon", "Goblin"])
        if isinstance(name_or_power, int):
            attack, health = name_or_power, name_or_power
        else:
            attack, health = 5, 5
        return CreatureCard(name, 5, "Rare", attack, health)

    def create_artifact(self, name_or_power=None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(["Mana Ring", "Crystal"])
        return ArtifactCard(name, 2, "Rare", 2, "Mana Boost")

    def create_spell(self, name_or_power=None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(["Fireball", "Lightning Bolt"])

        return SpellCard(name, 3, "Common", "Damage")

    def create_themed_deck(self, size: int) -> Dict:
        deck = []

        for _ in range(size):
            card = random.choice([
                self.create_creature(),
                self.create_spell(),
                self.create_artifact()
            ])
            deck.append(card)

        return {"deck": deck}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
