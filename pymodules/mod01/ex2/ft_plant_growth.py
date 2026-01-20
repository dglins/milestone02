#!/usr/bin/env python3
"""Module to register plants and simulate growth."""


class Plant:
    """Represents a plant with name, height (cm), and age (days)."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, cm: int = 1) -> None:
        """Increse height by cm"""
        self.height += cm

    def age_one_day(self, days: int = 1) -> None:
        """Incrise age by days"""
        self.age += days

    def day_pass(self) -> None:
        """Advance one day: grow 1 cm and age 1 day"""
        self.grow(1)
        self.age_one_day(1)

    def get_info(self) -> str:
        """Return representation of plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def grow_days(plant: Plant, days: int = 7) -> None:
    """Advance the plant by a number of days (default: 7)."""
    for _ in range(days - 1):
        plant.day_pass()


def run_cli(plant: Plant, days_to_grow: int = 7) -> None:
    """Creates a plant, simulates a week, and shows before/after."""
    print("\n\n=== Day 1 ===")
    print(plant.get_info())
    initial_hight: int = plant.height
    grow_days(plant, days_to_grow)
    print(f"=== Day {days_to_grow} ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - initial_hight}cm")


def main() -> None:
    """Runs my functions if main."""
    rose: Plant = Plant("Rose", 25, 30)
    run_cli(rose, 7)


if __name__ == "__main__":
    main()
