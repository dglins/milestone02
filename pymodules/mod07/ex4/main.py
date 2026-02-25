from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, Rarity.LEGENDARY, 1200
        )
    wizard = TournamentCard(
        "wizard_001", "Ice Wizard", 4, Rarity.EPIC, 1150
        )

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    print("Ice Wizard (ID: wizard_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")

    print("Creating tournament match...")
    match = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, c in enumerate(leaderboard, start=1):
        print(f"{i}. {c.name} - Rating: {c.rating} ({c.wins}-{c.losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
