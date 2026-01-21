#!/usr/bin/env python3
"""Module to inform about plants in the garden."""

plant: str = "Rose"
height_cm: int = 15
age_days: int = 42
output: str = f"""=== Welcome to My Garden ===
Plant: {plant}
Height: {height_cm}cm
Age: {age_days} days
=== End of Program ==="""
if __name__ == "__main__":
    print(output)
