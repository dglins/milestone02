#!/usr/bin/env python3
"""Module to inform about plants in the garden."""


def print_info_garden(plant: str, height_cm: int, age_days: int) -> None:
    """
    Displays information about a plant in your garden.
    """
    output: str = f"""=== Welcome to My Garden ===
Plant: {plant}
Height: {height_cm}cm
Age: {age_days} days
=== End of Program ==="""
    print(output)


if __name__ == "__main__":
    print_info_garden("Rose", 15, 42)
