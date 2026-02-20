#!/usr/bin/env python3


def ancient_sys(file_name: str = "ancient_fragment.txt") -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print()
    print(f"Accessing Storage Vault: {file_name}")
    file = None
    try:
        file = open(file_name)
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        output = file.read()
        print(output)
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    else:
        print("\nData recovery complete. Storage unit disconnected.")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    ancient_sys()
