from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    print(f'validate_ingredients("shadow dust"): {validate_ingredients("shadow dust")}')
    print()

    print("Testing spell recording (uses late import inside record_spell):")
    print(
        'record_spell("Flame Guard", "fire earth"): '
        f'{record_spell("Flame Guard", "fire earth")}'
    )
    print(
        'record_spell("Void Cloak", "moon ash"): '
        f'{record_spell("Void Cloak", "moon ash")}'
    )


if __name__ == "__main__":
    main()
