#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily.
You can run it with: python3 main.py or uv run python main.py

How it works:
1. It looks for your exercise files (like ft_plot_area.py) under a base folder
2. It imports them and calls their functions
3. If there's an error, it tells you what went wrong
"""

from __future__ import annotations

import argparse
import importlib
import shutil
import sys
from pathlib import Path
from typing import Iterable

EXERCISE_MAP: dict[str, Iterable[str]] = {
    "0": ("ft_hello_garden",),
    "1": ("ft_plot_area",),
    "2": ("ft_harvest_total",),
    "3": ("ft_plant_age",),
    "4": ("ft_water_reminder",),
    "5": ("ft_count_harvest_iterative", "ft_count_harvest_recursive"),
    "6": ("ft_garden_summary",),
    "7": ("ft_seed_inventory",),
    "a": (
        "ft_hello_garden",
        "ft_plot_area",
        "ft_harvest_total",
        "ft_plant_age",
        "ft_water_reminder",
        "ft_count_harvest_iterative",
        "ft_count_harvest_recursive",
        "ft_garden_summary",
        "ft_seed_inventory",
    ),
}


def _find_exercise_module(
    exercise_file_name: str, search_root: Path
) -> tuple[Path, Path]:
    """Return (module_path, module_dir) for a given exercise name."""
    try:
        module_path = next(search_root.rglob(f"{exercise_file_name}.py"))
    except StopIteration as error:
        msg = f"❌ Could not find {exercise_file_name}.py under {search_root}"
        raise FileNotFoundError(msg) from error
    return module_path, module_path.parent


def test_ft_exercise(exercise_file_name: str, search_root: Path) -> None:
    """
    Try to run one of your exercises.

    For example: test_ft_exercise("ft_plot_area") will:
    - Look for a file called ft_plot_area.py (searching recursively)
    - Import it
    - Call the function ft_plot_area() inside it
    """
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        module_path, module_dir = _find_exercise_module(
            exercise_file_name, search_root
        )
        module_dir_str = str(module_dir)
        if module_dir_str not in sys.path:
            sys.path.insert(0, module_dir_str)

        if exercise_file_name in sys.modules:
            del sys.modules[exercise_file_name]
        ft_module = importlib.import_module(exercise_file_name)

        ft_function = getattr(ft_module, exercise_file_name)

        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            ft_function()

    except FileNotFoundError:
        print(f"❌ Could not find {exercise_file_name}.py")
        print(f"   Searched under: {search_root}")
    except ImportError as error:
        print(f"❌ Could not import {exercise_file_name}: {error}")
    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}() in your file")
        print(f"   Make sure you have: def {exercise_file_name}():")
    except TypeError as error:
        msg = str(error)
        if "missing" in msg and "required positional argument" in msg:
            print(f"❌ Function signature error: {error}")
            print(
                "   For exercise 7, make sure your function takes parameters:"
            )
            print(
                f"   def {exercise_file_name}"
                "(seed_type: str, quantity: int, unit: str) -> None:"
            )
        else:
            print(f"❌ Type error: {error}")
            print("   Check your function parameters and types")
    except Exception as error:  # noqa: BLE001
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")
    else:
        print(f"✅ {exercise_file_name} completed (source: {module_path})")


def _print_menu() -> None:
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_plot_area        (Calculate garden plot area)")
    print("2 - ft_harvest_total    (Add up harvest weights)")
    print("3 - ft_plant_age        (Check if plant is ready)")
    print("4 - ft_water_reminder   (Check if plants need water)")
    print("5 - ft_count_harvest    (Iterative and recursive)")
    print("6 - ft_garden_summary   (Display garden info)")
    print("7 - ft_seed_inventory   (Seed inventory with type hints)")
    print("a - test all exercises")
    print()


def main(choice: str | None = None, search_root: Path | None = None) -> None:
    """Run the interactive tester."""
    search_root = search_root or Path.cwd()
    _print_menu()

    selected = choice or input("Enter your choice: ")
    targets = EXERCISE_MAP.get(selected)
    if not targets:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")
        return

    for exercise in targets:
        test_ft_exercise(exercise, search_root)


def cli() -> None:
    """CLI entry point for uv/pipx."""
    parser = argparse.ArgumentParser(
        description="Run the Growing Code exercise tester."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Base folder where exercises live (searched recursively). "
        "Defaults to the current working directory.",
    )
    parser.add_argument(
        "--choice",
        choices=tuple(EXERCISE_MAP.keys()),
        help="Exercise to run (skip to stay interactive).",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove all __pycache__ folders under --root after running.",
    )
    args = parser.parse_args()
    main(choice=args.choice, search_root=args.root)
    if args.clean:
        _clean_pycache(args.root)


def _clean_pycache(base: Path) -> None:
    """Remove all __pycache__ folders under a base path."""
    removed = 0
    for pycache_dir in base.rglob("__pycache__"):
        if pycache_dir.is_dir():
            shutil.rmtree(pycache_dir, ignore_errors=True)
            removed += 1
    print(f"🧹 Removed {removed} __pycache__ folder(s) under {base}")


if __name__ == "__main__":
    cli()
