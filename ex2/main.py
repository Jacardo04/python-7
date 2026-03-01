from ex2.EliteCard import EliteCard


def main():

    print("=== DataDeck Ability System ===\n")

    elite = EliteCard("Arcane Warrior", 6, "Epic", 5, 10, 4)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {elite.name} (Elite Card):")
    elite.play({})
    print()

    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(2))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
