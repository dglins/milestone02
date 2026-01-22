#!/usr/bin/env python3
"""Module to implement encapsulation."""


class SecurePlant:
    """Represents a plant and its internal state."""

    msg_sys = "=== Garden Security System ==="

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        print(SecurePlant.msg_sys)
        print(f"Plant created: {self.name}")

    # ===== INTERNAL MODIFIERS (PROTECTED) =====

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        print(f"Height updated: {height}cm [OK]")
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        print(f"Age updated: {age} days [OK]")
        self._age = age

    # ===== SAFE READ-ONLY ACCESS =====

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def __str__(self) -> str:
        return (
            f"Current plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)"
        )

    # ===== BEHAVIORS ======


def run_cli() -> None:
    plant = SecurePlant("Rose", height=10, age=5)

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-2)

    print(plant)


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()
