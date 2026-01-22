#!/usr/bin/env python3
"""Module to implement specialization."""


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


class Flower(Plant):
    """Specialized plant flower blueprint"""

    def __init__(self, name: str, height: int, age: int, special_atribute: str) -> None:
        super().__init__(name, height, age)
        self.color = special_atribute
        self.get_msg_type()
        self.bloom()

    def get_msg_type(self) -> str:
        print(f"{self}, {self.color} color")

    def bloom(self) -> str:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """Specialized plant tree blueprint"""

    def __init__(self, name: str, height: int, age: int, special_atribute: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = special_atribute
        self.get_msg_type()
        self.produce_shade()

    def get_msg_type(self) -> str:
        print(f"{self} {self.trunk_diameter} diameter")

    def produce_shade(self) -> str:
        shade: int = self.trunk_diameter + (self._height / 70)
        print(f"{self.name} provides {shade:.0f} square meters of shade\n")


class Vegetable(Plant):
    """Specialized plant vegetable blueprint"""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        special_atribute: str,
        special_atribute2: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = special_atribute
        self.nutritional_value = special_atribute2
        self.get_msg_type()
        self.get_nutrition()

    def get_msg_type(self) -> str:
        print(f"{self} {self.harvest_season} harvest")

    def get_nutrition(self) -> str:
        print(f"{self.name} is rich in {self.nutritional_value}\n")


def run_cli() -> None:
    print("\n=== Garden Plant Types ===\n")
    Flower("Rose", 10, 5, "azul")
    Flower("Tulip", 12, 5, "purple")

    Tree("Oak", 400, 50, 40)
    Tree("Apple tree", 280, 20, 60)

    Vegetable("Carrot", 8, 20, "summer", "Vitamin C")
    Vegetable("Potato", 5, 50, "winter", "Vitamin B")


def main() -> None:
    run_cli()


if __name__ == "__main__":
    main()
