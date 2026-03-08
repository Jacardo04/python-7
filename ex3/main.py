from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")

    print(f"Hand: {[str(card) for card in engine.hand]}\n")

    print("Turn execution:")
    result = engine.simulate_turn()

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {result}\n")

    print("Game Report:")
    report = engine.get_engine_status()
    print(report)

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
