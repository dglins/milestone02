from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")

    for base in EliteCard.__bases__:
        methods = [
            name
            for name, value in base.__dict__.items()
            if callable(value) and not name.startswith("_")
        ]
        print(f"- {base.__name__}: {methods}")
    print()

    print("Playing Arcane Warrior (Elite Card):")
    elite = EliteCard("Arcane Warrior", 4, Rarity.EPIC)
    print()

    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    elite.channel_mana(4)
    print(f"Mana channel: {elite.channel_mana(3)}")
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
