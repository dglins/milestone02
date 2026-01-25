#!/usr/bin/env python3
"""
$> python3 ft_different_errors.py
=== Garden Error Types Demo ===
Testing ValueError...
Caught ValueError: invalid literal for int()
Testing ZeroDivisionError...
Caught ZeroDivisionError: division by zero
Testing FileNotFoundError...
Caught FileNotFoundError: No such file 'missing.txt'
Testing KeyError...
Caught KeyError: 'missing\_plant'
Testing multiple errors together...
Caught an error, but program continues!
All error types tested successfully!
"""


def garden_operations(type_error: str) -> None:
    match type_error:
        case "ValueError":
            try:
                int("abc")
            except ValueError as error:
                return error
        case "ZeroDivisionError":
            try:
                x = 4 / 0
            except ZeroDivisionError as error:
                return error
        case "FileNotFoundError":
            try:
                open("file.txt")
            except FileNotFoundError as error:
                return error
            finally:
                close("file.txt")
        case "KeyError":
            try:
                my_dict = {"try_this: 0"}


def test_temperature_input() -> None:
    print("\n=== Garden Error Types Demo ===\n")
    temp_str: str = "25"
    print(f"\nTesting temperature: {temp_str}")
    check_temperature(temp_str)
    temp_str: str = "abc"
    print(f"\nTesting temperature: {temp_str}")
    check_temperature(temp_str)
    temp_str: str = "100"
    print(f"\nTesting temperature: {temp_str}")
    check_temperature(temp_str)
    temp_str: str = "-50"
    print(f"\nTesting temperature: {temp_str}")
    check_temperature(temp_str)


if __name__ == "__main__":
    test_temperature_input()
