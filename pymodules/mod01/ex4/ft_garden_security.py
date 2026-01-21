#!/usr/bin/env python3
"""Module to implement a factory."""


class Plant:
    """Represents a plant with name, height (cm), and age (days)."""

    def __init__(self, name: str, in_height: int, in_age: int) -> None:
        """Initialize plant."""
        self.name: str = name
        self.in_height: int = in_height
        self.in_age: int = in_age

    def grow(self, cm: int = 1) -> None:
        """Increse height by cm"""
        self.in_height += cm

    def age(self, days: int = 1) -> None:
        """Incrise age by days"""
        self.in_age += days

    def day_pass(self) -> None:
        """Advance one day: grow 1 cm and age 1 day"""
        self.grow(1)
        self.age(1)

    def get_info(self) -> dict[str, str]:
        """Return informations of plant."""
        return self.__dict__

    def __str__(self) -> str:
        """Return representation of plant."""
        return f"{self.name}: {self.in_height}cm, {self.in_age} days old"

    def grow_days(self, days: int = 7) -> None:
        """Advance the plant by a number of days (default: 7)."""
        for _ in range(days - 1):
            self.day_pass()

    @classmethod
    def plant_factory(cls, list_plants: list[tuple[str, int, int]]) -> None:
        print("\n\n=== Plant Factory Output ===")
        total_plants = 0
        for name_inl, in_age_inl, in_height_inl in list_plants:
            cls(name_inl, in_age_inl, in_height_inl)
            print(f"Created: {name_inl} ({in_height_inl}cm, {in_age_inl} days)")
            total_plants += 1
        print(f"\nTotal plants created: {total_plants}")


def run_cli() -> None:
    """Creates plants using Factory."""
    list_of_plants: list[tuple[str, int, int]] = [
        ("Rose", 10, 2),
        ("Tomato", 2, 9),
        ("Banana", 4, 8),
        ("Peach", 89, 9),
        ("Sunflower", 10, 92),
    ]
    Plant.plant_factory(list_of_plants)


def main() -> None:
    """Tests code using cli."""
    run_cli()


if __name__ == "__main__":
    main()
