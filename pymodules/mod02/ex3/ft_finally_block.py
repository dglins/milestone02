#!/usr/bin/env python3


def water_plants(plant_list: list[str | None]) -> None:
    try:
        print("Opening watering system")

        for plant in plant_list:
            if plant is None:
                return print("Cannot water None - invalid plant!")

            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    try:
        print("=== Garden Watering System ===")

        print()
        print("Testing normal watering...")
        good_plants: list[str | None] = ["tomato", "lettuce", "carrots"]
        water_plants(good_plants)
        print("Watering completed successfully!")

        print()
        print("Testing with error...")
        bad_plants: list[str | None] = ["tomato", None, "carrots"]
        water_plants(bad_plants)
    finally:
        print()
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
