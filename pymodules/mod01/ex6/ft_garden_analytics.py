#!/usr/bin/env python3
"""Module to implement nested components and inheritance chains."""


class Plant:
    """Represents a plant and its internal state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)

    # ===== INTERNAL MODIFIERS (PROTECTED) =====

    def set_height(self, height: int) -> None:
        self._height = height

    def set_age(self, age: int) -> None:
        self._age = age

    # ===== SAFE READ-ONLY ACCESS =====

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_class(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.get_class()}): "
            f"{self.get_height()}cm, "
            f"{self.get_age()} days"
        )


class FloweringPlant(Plant):
    """Specialized plant blueprint"""

    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)
        self.get_msg_type()

    def get_msg_type(self) -> str:
        print(f"{self}, {self.color} color")


class PrizeFlower(FloweringPlant):
    """Specialized floweringplant blueprint"""

    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)
        self.get_msg_type()

    def get_msg_type(self) -> str:
        print(f"{self} {self.trunk_diameter} diameter")


class GardenManager:
    """Specialized plant vegetable blueprint"""

    def get_msg_type(self) -> str:
        print(f"{self} {self.harvest_season} harvest")

    def get_nutrition(self) -> str:
        print(f"{self.name} is rich in {self.nutritional_value}\n")


def run_cli() -> None:
    print("\n=== Garden Plant Types ===\n")


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()
