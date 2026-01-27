#!/usr/bin/env python3

# =====================
# Custom Exceptions
# =====================


class GardenError(Exception):
    """Base garden error"""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


# =====================
# Garden Manager
# =====================


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    # -----------------
    # Add plants
    # -----------------

    def add_plant(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[name] = {
            "water": 5,
            "sun": 8,
        }

    # -----------------
    # Water plants
    # -----------------

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    # -----------------
    # Plant health
    # -----------------

    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


# =====================
# Tests
# =====================


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    # -----------------
    # Adding plants
    # -----------------

    print("Adding plants to garden...")
    for plant in ("tomato", "lettuce", ""):
        try:
            garden.add_plant(plant)
            print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    # -----------------
    # Watering
    # -----------------

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Water error: {e}")

    # -----------------
    # Health check
    # -----------------

    print("Checking plant health...")
    garden.plants["lettuce"]["water"] = 15
    for plant in ("tomato", "lettuce"):
        try:
            garden.check_plant_health(plant)
        except ValueError as e:
            print(f"Error checking {plant}: {e}")

    # -----------------
    # Error recovery
    # -----------------

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
