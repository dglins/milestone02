#!/usr/bin/env python3


def ft_write_discovery(file_name: str = "new_discovery.txt") -> None:
    dest = None
    src = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    try:
        print(f"\nInitializing new storage unit: {file_name}")
        dest = open(file_name, "x", encoding="utf-8")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        sep = "\n"
        entry = 1
        for line in src:
            dest.write(line + sep)
            print(f"[ENTRY {entry:03d}] ", line)
            entry += 1

        print("\nData inscription complete. Storage unit sealed.")

    except FileExistsError:
        print("File already in Archive. We can't overwrite!")

    else:
        print(f"Archive '{file_name}' ready for long-term preservation.")

    finally:
        if dest:
            dest.close()


if __name__ == "__main__":
    ft_write_discovery()
