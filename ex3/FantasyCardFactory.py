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
