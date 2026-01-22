#!/usr/bin/env python3
"""Module to implement encapsulation with a secure facade."""


class Plant:
    """Represents a plant and its internal state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    # ===== INTERNAL MODIFIERS (PROTECTED) =====

    def _set_height(self, height: int) -> None:
        self._height = height

    def _set_age(self, age: int) -> None:
        self._age = age

    def _grow(self, cm: int = 1) -> None:
        self._height += cm

    def _age_days(self, days: int = 1) -> None:
        self._age += days

    # ===== SAFE READ-ONLY ACCESS =====

    @property
    def height(self) -> int:
        return self._height

    @property
    def age(self) -> int:
        return self._age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


class SecurePlant:
    """
    Secure facade for Plant.
    Ensures data integrity through validation.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self._plant = Plant(name, 0, 0)
        self.set_height(height)
        self.set_age(age)

    # ===== VALIDATED SETTERS =====

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Error: height cannot be negative.")
            return
        self._plant._set_height(height)

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Error: age cannot be negative.")
            return
        self._plant._set_age(age)

    # ===== SAFE GETTERS =====

    def get_height(self) -> int:
        return self._plant.height

    def get_age(self) -> int:
        return self._plant.age

    def get_name(self) -> str:
        return self._plant.name

    # ===== CONTROLLED BEHAVIOR =====

    def grow(self, cm: int = 1) -> None:
        if cm <= 0:
            print("Error: growth must be positive.")
            return
        self._plant._grow(cm)

    def pass_days(self, days: int = 1) -> None:
        if days <= 0:
            print("Error: days must be positive.")
            return
        for _ in range(days):
            self._plant._age_days(1)
            self._plant._grow(1)

    def info(self) -> str:
        return str(self._plant)


def run_cli() -> None:
    plant = SecurePlant("Rose", height=10, age=5)

    print(plant.info())

    plant.grow(3)
    plant.pass_days(2)

    print(plant.info())

    plant.set_height(-5)
    plant.set_age(-2)

    print(plant.info())


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()
