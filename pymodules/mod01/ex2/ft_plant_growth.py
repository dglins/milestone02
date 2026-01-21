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

    def get_info(self) -> dict[str, int | str]:
        """Return informations of plant."""
        return self.__dict__

    def __str__(self) -> str:
        """Return representation of plant."""
        return f"{self.name}: {self.initial_height}cm, {self.initial_age} days old"

    def grow_days(self, days: int = 7) -> None:
        """Advance the plant by a number of days (default: 7)."""
        print("\n\n=== Day 1 ===")
        print(self)
        init_height: int = self.initial_height
        for _ in range(days - 1):
            self.day_pass()
        print(f"=== Day {days} ===")
        print(f"Growth this week: +{self.initial_height - init_height}cm")


def run_cli() -> None:
    """Simulates growth for a set of plants."""
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tomato", 3, 10),
        Plant("Banana", 12, 6),
        Plant("Peach", 2, 3),
    ]
    for plant in plants:
        plant.grow_days(7)


def main() -> None:
    """Runs my functions if main."""
    run_cli()


if __name__ == "__main__":
    main()
