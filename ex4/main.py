from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    """the registered cards"""
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 6, 1150)
    platform.reg_card(dragon)
    platform.reg_card(wizard)

    print("Registering Tournament Cards...\n")
    for c in [dragon, wizard]:
        print(f"{c.name} (ID: {c.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {c.rating}")
        print(f"- Record: {c.wins}-{c.losses}\n")

    """the matrix"""
    print("Creating tournament match...")
    match_result = platform.create_match(dragon.card_id, wizard.card_id)
    print(f"Match result: {match_result}")

    """leaderboard"""
    print("Tournament Leaderboard:")
    for i, c in enumerate(platform.get_leaderboard(), 1):
        print(
            f"{i}. {c['name']} - Rating: {c['rating']} "
            f"({c['wins']}-{c['losses']})"
        )

    """tourney report"""
    report = platform.generate_tournament_report()
    print("\nPlatform Report:")
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()
