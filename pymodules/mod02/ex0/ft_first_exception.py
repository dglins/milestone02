#!/usr/bin/env python3


def check_temperature(temp_str: str) -> None:
    try:
        temp_int: int = int(temp_str)
        if temp_int < 0 or temp_int > 40:
            if temp_int < 0:
                print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
            elif temp_int > 40:
                print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    try:
        print("\n=== Garden Temperature Checker ===\n")

        temp_str: str = "25"
        print()
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)

        temp_str: str = "abc"
        print()
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)

        temp_str: str = "100"
        print()
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)

        temp_str: str = "-50"
        print()
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)

    except Exception:
        return print("something wrong!")
    else:
        print()
        return print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
