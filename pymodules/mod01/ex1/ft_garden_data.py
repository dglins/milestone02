#!/usr/bin/env python3
"""Module to registry plants using a class."""


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


def main() -> None:
    """Runs my functions if main."""
    run_cli()


if __name__ == "__main__":
    main()
