from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 2)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    game_state = {"mana": 6}
    play_result = fire_dragon.play(game_state)
    print(f"Play result: {play_result}\n")

    attack_result = fire_dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
