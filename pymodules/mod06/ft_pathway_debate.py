from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import elixir_of_life, philosophers_stone


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")
    print()

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


if __name__ == "__main__":
    main()
