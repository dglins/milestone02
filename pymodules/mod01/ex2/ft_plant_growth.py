#!/usr/bin/env python3
"""Module to simulate growth."""


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


def run_cli(plant: Plant, days_to_grow: int = 7) -> None:
    """Creates a plant, simulates a week, and shows before/after."""
    print("\n\n=== Day 1 ===")
    print(plant)
    init_height: int = plant.initial_height
    plant.grow_days(days_to_grow)
    print(f"=== Day {days_to_grow} ===")
    print(plant)
    print(f"Growth this week: +{plant.initial_height - init_height}cm")


def main() -> None:
    """Runs my functions if main."""
    rose: Plant = Plant("Rose", 25, 30)
    run_cli(rose, 7)
    tomato: Plant = Plant("Tomato", 3, 10)
    run_cli(tomato, 7)
    banana: Plant = Plant("Banana", 12, 6)
    run_cli(banana, 7)
    peach: Plant = Plant("Peach", 2, 3)
    run_cli(peach, 7)


if __name__ == "__main__":
    main()
