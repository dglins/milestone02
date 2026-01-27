#!/usr/bin/env python3
"""Module to implement arguments using sys.argv"""

import sys


def ft_command_quest(args: list[str]) -> None:
    """Function that takes arguments from argv"""
    print("=== Command Quest ===")

    arguments: int = len(args)

    if arguments < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arguments}")

        for i in range(1, len(args)):
            print(f"arg {i} : {args[i]}")

    print(f"Program name: {args[0]}")
    print(f"Total arguments: {arguments}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
