#!/usr/bin/env python3
"""Module to register plants and simulate growth."""


class SecurePlant:
    def set_height(): ...

    def set_age(): ...

    def get_height(): ...

    def get_age(): ...


class Plant:
    """Represents a plant with name, height (cm), and age (days)."""

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
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
        """Return current status of plant."""
        return self.name, self.height, self.age


def grow_days(plant: Plant, days: int = 7) -> None:
    """Advance the plant by a number of days (default: 7)."""
    for _ in range(days - 1):
        plant.day_pass()


def run_cli(plants: list[Plant]) -> None:
    """Creates plants and shows all my plants created."""
    print("\n\n=== Plant Factory Output ===")
    total_plants = 0
    for plant in plants:
        name, height, days = plant.get_info()
        print(f"Created: {name} ({height}cm, {days} days)")
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


def main() -> None:
    """Runs my functions at if main."""
    list_of_plants: list[Plant] = [
        Plant("Rose", 10, 2),
        Plant("Tomato", 2, 9),
        Plant("Banana", 4, 8),
        Plant("Peach", 89, 9),
        Plant("Sunflower", 10, 92),
    ]
    run_cli(list_of_plants)


if __name__ == "__main__":
    main()
