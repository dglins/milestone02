#!/usr/bin/env python3


class GardenError(Exception):
    """Base class for all garden-related errors."""

    pass


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


# Functions that raise custom errors


def garden_operations(error_type: str) -> None:
    match error_type:
        case "PlantError":
            raise PlantError

        case "WaterError":
            raise WaterError

        case _:
            raise GardenError("Unknown garden problem!")


def test_custom_errors() -> None:
    print("\n=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        garden_operations("PlantError")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        garden_operations("WaterError")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    for test in ("PlantError", "WaterError"):
        try:
            garden_operations(test)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
