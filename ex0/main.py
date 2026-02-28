from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon.attack_target(goblin))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
