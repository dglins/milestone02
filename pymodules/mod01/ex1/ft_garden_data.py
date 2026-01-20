#!/usr/bin/env python3
"""Module to registry plants."""


class Plant:
    """Represents plants. its name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """Return representation of plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def run_cli() -> None:
    """Creates and shows plants."""
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant)


def run_cli_input() -> None:
    """Creates and shows plants with input."""
    name = input("Plant: ")
    height = input("Height: ")
    age = input("Age: ")
    plant = Plant(name, height, age)
    print("=== Garden Plant Registry ===")
    print(plant)


def main() -> None:
    """Runs my functions if main."""
    run_cli()
    run_cli_input()


if __name__ == "__main__":
    main()
