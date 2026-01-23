#!/usr/bin/env python3
"""Garden Management System Demo"""


# =========================
# Plant hierarchy
# =========================


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def grow(self, cm: int = 1) -> None:
        self._height += cm
        print(f"{self.name} grew {cm}cm")

    @property
    def height(self) -> int:
        return self._height

    def describe(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def describe(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
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
            plant.grow(1)
            self._total_growth += 1

    def list_plants(self) -> None:
        print("Plants in garden:")
        for plant in self._plants:
            print(f"- {plant.describe()}")

    def get_plants(self) -> list[Plant]:
        return list(self._plants)

    @property
    def total_growth(self) -> int:
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
            score = garden.total_growth * 10
            for plant in garden.get_plants():
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 10
                score += plant.height
            return score


# =========================
# Demo
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
        f"Plants added: {len(alice.get_plants())}, Total growth: {alice.total_growth}cm"
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
