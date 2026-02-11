#!/usr/bin/env python3


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("Initiating crisis management protocol...")

    # Scenario 1:
    print("\n--- Attempting access to standard_archive.txt ---")
    try:
        with open("standard_archive.txt", "r") as file:
            content = file.read()
            print(
                f"[CRISIS ALERT] Standard archive accessed. Content: {content}"
            )
            print(
                "[RESPONSE] Standard archive recovery successful. "
                "System stability maintained."
            )
    except Exception as e:
        print(
            f"[CRISIS ALERT] Failed to access standard_archive.txt. Error: {e}"
        )
        print("[RESPONSE] Emergency protocol initiated for standard archive.")

    # Scenario 2:
    print("\n--- Attempting access to non_existent_archive.txt ---")
    try:
        with open("non_existent_archive.txt", "r") as file:
            content = file.read()
            print(
                "[CRISIS ALERT] Non-existent archive accessed. "
                f"Content: {content}"
            )
            print(
                "[RESPONSE] Unexpected data found in non-existent archive. "
                "Investigate immediately."
            )
    except FileNotFoundError:
        print(
            "[CRISIS ALERT] Target non_existent_archive.txt not found in "
            "storage matrix."
        )
        print(
            "[RESPONSE] Failsafe protocol: Archive missing. "
            "Initiating data reconstruction query."
        )
    except Exception as e:
        print(
            "[CRISIS ALERT] Unexpected error during access "
            f"to non_existent_archive.txt. Error: {e}"
        )
        print("[RESPONSE] Emergency protocol initiated for missing archive.")

    # Scenario 3:
    print(
        "\n--- Attempting access to a restricted system directory (/root) ---"
    )
    try:
        with open("/root", "r") as file:
            content = file.read()
            print(
                f"[CRISIS ALERT] Restricted vault accessed. Content: {content}"
            )
            print(
                "[RESPONSE] Security breach detected! "
                "Immediate lockdown initiated."
            )
    except PermissionError:
        print(
            "[CRISIS ALERT] Access denied to restricted system directory "
            "(/root). Security protocol violation detected."
        )
        print(
            "[RESPONSE] Failsafe protocol: "
            "Unauthorized access attempt blocked. Security incident logged."
        )
    except FileNotFoundError:
        print("[CRISIS ALERT] Target /root not found (unexpected).")
        print("[RESPONSE] Initiating system integrity check.")
    except Exception as e:
        print(
            "[CRISIS ALERT] Unexpected error during access to "
            f"restricted system directory. Error: {e}"
        )
        print("[RESPONSE] Emergency protocol initiated for security breach.")

    # Scenario 4:
    print("\n--- Attempting access to malformed_data.txt ---")
    try:
        with open("malformed_data.txt", "r") as file:
            content = file.read()
            print(
                "[CRISIS ALERT] Malformed data archive accessed. "
                f"Content: {content}"
            )
            print(
                "[RESPONSE] Data integrity compromised. "
                "Initiating repair protocols."
            )
    except UnicodeDecodeError:
        print(
            "[CRISIS ALERT] Malformed data detected in malformed_data.txt. "
            "UnicodeDecodeError during read."
        )
        print(
            "[RESPONSE] Failsafe protocol: Data format anomaly. "
            "Isolating and analyzing corrupted sector."
        )
    except Exception as e:
        print(
            "[CRISIS ALERT] Unexpected system anomaly accessing "
            f"malformed_data.txt. Error: {e}"
        )
        print(
            "[RESPONSE] Failsafe protocol: Unforeseen error. "
            "Activating diagnostic suite."
        )

    print("\nCrisis response operations complete. System status: Vigilant.")


if __name__ == "__main__":
    ft_crisis_response()
