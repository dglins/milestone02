#!/usr/bin/env python3
"""Module to implement a factory."""


class Plant:
    """Represents a plant with name, height (cm), and age (days)."""


class Plant:
    """Represents a plant with name, height (cm), and age (days)."""

    def __init__(self, name: str, initial_height: int, initial_age: int) -> None:
        """Initialize plant."""
        self.name: str = name
        self.initial_height: int = initial_height
        self.initial_age: int = initial_age

    def grow(self, cm: int = 1) -> None:
        """Increse height by cm"""
        self.initial_height += cm

    def age(self, days: int = 1) -> None:
        """Incrise age by days"""
        self.initial_age += days

    def day_pass(self) -> None:
        """Advance one day: grow 1 cm and age 1 day"""
        self.grow(1)
        self.age(1)

    def get_info(self) -> dict[str, str]:
        """Return informations of plant."""
        return self.__dict__

    def __str__(self) -> str:
        """Return representation of plant."""
        return f"{self.name}: {self.initial_height}cm, {self.initial_age} days old"

    def grow_days(self, days: int = 7) -> None:
        """Advance the plant by a number of days (default: 7)."""
        for _ in range(days - 1):
            self.day_pass()

    @classmethod
    def plant_factory(cls, name: str, initial_age: int, initial_height: int) -> Plant:
        print(f"Created: {name} ({initial_height}cm, {initial_age} days)")
        return cls(name, initial_age, initial_height)


def run_cli(list_plants: list[tuple[str, int, int]]) -> None:
    """Creates plants using Factory and shows how many plants was created."""
    print("\n\n=== Plant Factory Output ===")
    total_plants = 0
    for name, initial_age, initial_height in list_plants:
        Plant.plant_factory(name, initial_age, initial_height)
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


def main() -> None:
    """Tests code using cli."""
    list_of_plants: list[tuple[str, int, int]] = [
        ("Rose", 10, 2),
        ("Tomato", 2, 9),
        ("Banana", 4, 8),
        ("Peach", 89, 9),
        ("Sunflower", 10, 92),
    ]
    run_cli(list_of_plants)


if __name__ == "__main__":
    main()
