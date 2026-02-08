import alchemy.elements
from alchemy.elements import create_fire
from alchemy.elements import create_fire as conjure_fire, create_water
from alchemy.potions import healing_potion as heal


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()

    print("Method 2 - Specific function import:")
    print(f"create_fire(): {create_fire()}")
    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    print("Method 4 - Multiple imports:")
    print(f"conjure_fire(): {conjure_fire()}")
    print(f"create_water(): {create_water()}")


if __name__ == "__main__":
    main()
