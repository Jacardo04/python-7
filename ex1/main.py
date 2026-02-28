from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    # Create cards
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Common",
                               "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3,
                                "Permanent: +1 mana per turn")

    # Build deck
    deck = Deck()
    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    # Show deck stats
    print("Deck stats:", {
        "total_cards": deck.deck_size(),
        "creatures": sum(isinstance(c, CreatureCard) for c in deck.cards),
        "spells": sum(isinstance(c, SpellCard) for c in deck.cards),
        "artifacts": sum(isinstance(c, ArtifactCard) for c in deck.cards),
        "avg_cost": round(sum(c.cost for c in deck.cards) / deck.deck_size())
    })

    # Shuffle and play
    print("\nDrawing and playing cards:\n")
    deck.shuffle()

    while deck.deck_size() > 0:
        card = deck.draw_card()
        card_type = type(card).__name__
        print(f"Drew: {card.name} ({card_type})")
        print("Play result:", card.play({}))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
