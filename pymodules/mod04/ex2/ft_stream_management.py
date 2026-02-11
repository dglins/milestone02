#!/usr/bin/env python3

import sys


def ft_stream_management() -> None:

    try:
        sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

        print()
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        archivist_id = input()
        sys.stdout.write("Input Stream active. Enter status report: ")
        status_report = input()

        print()
        sys.stdout.write(
            f"[STANDARD] Archive status from {archivist_id}: {status_report}\n"
        )
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n"
        )
        sys.stdout.write("[STANDARD] Data transmission complete\n")

        print()
        sys.stdout.write("Three-channel communication test successful.\n")
    except Exception:
        print("Something is wrong!")


if __name__ == "__main__":
    ft_stream_management()
