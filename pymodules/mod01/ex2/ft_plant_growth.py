class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def growing(self):
        self.height += 1

    def aging(self):
        self.age += 1

    def __repr__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    for day in days:
        print(f"=== Day {day} ===")

    for plant in plants:
        print(plant)


if __name__ == "__main__":
    main()
