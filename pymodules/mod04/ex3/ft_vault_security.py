#!/usr/bin/env python3


def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as vault_file:
            classified_data = vault_file.read()
            print(f"[CLASSIFIED] {classified_data}")
        print("[STANDARD] Data extraction successful. Vault sealed.")
    except FileNotFoundError:
        print(
            "[ALERT] Classified data file not found. Vault sealed with error."
        )
    except Exception as e:
        print(f"[ALERT] Error during data extraction: {e}. Vault sealed.")

    # Secure Preservation (Writing)
    print("\nSECURE PRESERVATION:")
    try:
        with open("access_log.txt", "a") as vault_log:
            vault_log.write(
                "Access granted for archivist at "
                + str(__import__("datetime").datetime.now())
                + "\n"
            )
            print("[STANDARD] Access log updated.")
        print("[STANDARD] Data preservation successful. Vault sealed.")
    except Exception as e:
        print(f"[ALERT] Error during data preservation: {e}. Vault sealed.")

    print("\nSecure vault operations complete.")
    print("Vault connection terminated.")


if __name__ == "__main__":
    ft_vault_security()
