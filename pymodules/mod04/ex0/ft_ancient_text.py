#!/usr/bin/env python3


def ancient_sys(file_name: str = "ancient_fragment.txt"):
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    file = None
    try:
        file = open(f"{file_name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        output = file.read()
        print(output)
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    else:
        print("\nData recovery complete. Storage unit disconnected.")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    ancient_sys()
