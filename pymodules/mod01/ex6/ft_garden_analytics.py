#!/usr/bin/env python3
"""Garden Management System Demo"""


# =========================
# Plant hierarchy
# =========================


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def set_height(self, cm: int = 1) -> None:
        self._height += cm
        print(f"{self.name} grew {cm}cm")

    def get_height(self) -> int:
        return self._height

    def describe(self) -> str:
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def describe(self) -> str:
        return (
            f"{self.name}: {self.get_height()}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self._prize_points = prize_points

    def get_prize_points(self) -> int:
        return self._prize_points

    def describe(self) -> str:
        return (
            f"{self.name}: {self.get_height()}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.get_prize_points()}"
        )


# =========================
# Garden
# =========================


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._plants: list[Plant] = []
        self._total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self._plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self._plants:
            plant.set_height(1)
            self._total_growth += 1

    def list_plants(self) -> None:
        print("Plants in garden:")
        for plant in self._plants:
            print(f"- {plant.describe()}")

    def get_plants(self) -> list[Plant]:
        return self._plants

    def get_total_growth(self) -> int:
        return self._total_growth


# =========================
# Garden Manager
# =========================


class GardenManager:
    def __init__(self) -> None:
        self._gardens: dict[str, Garden] = {}

    # -------- Instance methods --------

    def add_garden(self, garden: Garden) -> None:
        self._gardens[garden.owner] = garden

    def get_garden(self, owner: str) -> Garden:
        return self._gardens[owner]

    def total_gardens(self) -> int:
        return len(self._gardens)

    # -------- Class method --------

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.add_garden(Garden(owner))
        return manager

    # -------- Static utility methods --------

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    # -------- Nested helper --------

    class GardenStats:
        @staticmethod
        def plant_counts(garden: Garden) -> dict[str, int]:
            regular = flowering = prize = 0
            for plant in garden.get_plants():
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return {
                "regular": regular,
                "flowering": flowering,
                "prize": prize,
            }

        @staticmethod
        def garden_score(garden: Garden) -> int:
            score = garden.get_total_growth() * 10
            for plant in garden.get_plants():
                if isinstance(plant, PrizeFlower):
                    score += plant.get_prize_points() * 10
                score += plant.get_height()
            return score


# =========================
# Cli
# =========================


def main() -> None:
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice = manager.get_garden("Alice")
    bob = manager.get_garden("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", prize_points=10))

    alice.help_plants_grow()

    print("=== Alice's Garden Report ===")
    alice.list_plants()

    stats = GardenManager.GardenStats
    counts = stats.plant_counts(alice)

    print(
        f"Plants added: {len(alice.get_plants())}, "
        f"Total growth: {alice.get_total_growth()}cm"
    )
    print(
        f"Plant types: {counts['regular']} regular, "
        f"{counts['flowering']} flowering, "
        f"{counts['prize']} prize flowers"
    )

    print(
        "Height validation test:",
        GardenManager.validate_height(10),
    )

    alice_score = stats.garden_score(alice)
    bob_score = stats.garden_score(bob)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.total_gardens()}")


if __name__ == "__main__":
    main()
