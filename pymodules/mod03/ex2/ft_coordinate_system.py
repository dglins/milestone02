#!/usr/bin/env python3

import math
import sys


class CoordinateSystem:
    def __init__(self, argv: list[str]) -> None:
        self.argv = argv
        self.origin: tuple[int, int, int] = (0, 0, 0)

    def run(self) -> None:
        print("=== Game Coordinate System ===")

        position: tuple[int, int, int] | None = self._parse_arguments()
        if not position:
            return

        print(f"Position created: {position}")
        print(
            f"Distance between {self.origin} and {position}: "
            f"{self._distance(self.origin, position):.2f}"
        )

        self._unpack(position)

    def _parse_arguments(self) -> tuple[int, int, int] | None:
        if len(self.argv) != 4:
            print(
                "Usage: python ft_coordinate_system.py "
                "<x: int> <y: int> <z: int>"
            )
            return None

        coords: list[int] = []

        for arg in self.argv[1:]:
            try:
                coords += [int(arg)]
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")
                print(
                    f"Error details - Type: {e.__class__.__name__}, Args: ({
                        e
                    })"
                )
                return None
        coords_tuple: tuple[int, int, int] = tuple(coords)
        return coords_tuple

    def _distance(
        self, p1: tuple[int, int, int], p2: tuple[int, int, int]
    ) -> float:
        x1, y1, z1 = p1
        x2, y2, z2 = p2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def _unpack(self, pos: tuple[int, int, int]) -> None:
        x, y, z = pos
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    app = CoordinateSystem(sys.argv)
    app.run()


if __name__ == "__main__":
    main()
