#!/usr/bin/env python3


class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name: str = name
        self.achievements: set[str] = achievements


class AchievementSystem:
    def __init__(self, players: list[Player]) -> None:
        self.players: list[Player] = players

    def run(self) -> None:
        print("\n=== Achievement Tracker System ===")

        for p in self.players:
            print(f"Player {p.name} achievements: {p.achievements}")

        print("\n=== Achievement Analytics ===")
        self.analytics()

    def analytics(self) -> None:
        all_achievements: set[str] = self.players[0].achievements
        for p in self.players[1:]:
            all_achievements = all_achievements.union(p.achievements)

        print(f"All unique achievements: {all_achievements}")
        print(f"Total unique achievements: {len(all_achievements)}")

        common: set[str] = self.players[0].achievements
        for p in self.players[1:]:
            common = common.intersection(p.achievements)

        print(f"Common to all players: {common}")

        shared: set[str] = set()
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                shared = shared.union(
                    self.players[i].achievements.intersection(
                        self.players[j].achievements
                    )
                )

        rare: set[str] = all_achievements.difference(shared)
        print(f"Rare achievements (1 player): {rare}")


def main() -> None:
    alice = Player(
        "alice",
        set(("first_kill", "level_10", "treasure_hunter", "speed_demon")),
    )
    bob = Player(
        "bob", set(("first_kill", "level_10", "boss_slayer", "collector"))
    )
    charlie = Player(
        "charlie",
        set(
            (
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist",
            )
        ),
    )

    players = [alice, bob, charlie]

    system = AchievementSystem(players)
    system.run()


if __name__ == "__main__":
    main()
