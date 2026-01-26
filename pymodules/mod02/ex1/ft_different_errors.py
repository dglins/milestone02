#!/usr/bin/env python3


def garden_operations(error_type: str) -> None:
    """Generates erros types. Depends on error_type."""
    match error_type:
        case "ValueError":
            int("abc")

        case "ZeroDivisionError":
            _ = 10 / 0

        case "FileNotFoundError":
            f = None
            try:
                f = open("missing.txt")
            finally:
                if f is not None:
                    f.close()

        case "KeyError":
            {"roses": 5}["missing/_plant"]

        case _:
            raise ValueError("Unknown error type")


def test_error_types() -> None:
    """Tests garden_operations. Shows error messages."""
    print("=== Garden Error Types Demo ===")

    tests = (
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError",
    )

    for test in tests:
        try:
            print(f"\nTesting {test}...")
            garden_operations(test)

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: No such file '{e.filename}'")

        except KeyError as e:
            print(f"Caught KeyError: {e.args[0]!r}")

        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e.args[0]}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
