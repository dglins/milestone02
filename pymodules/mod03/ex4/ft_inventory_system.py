#!/usr/bin/env python3

import sys


class InventoryMaster:
    def __init__(self, initial_inventory: dict[str, int]) -> None:
        self.inventory: dict[str, int] = {}
        if initial_inventory:
            self.inventory.update(initial_inventory)

    def get_total_items(self) -> int | None:
        """
        Calculates and returns the total number of all items in the inventory.
        """
        return sum(self.inventory.values())

    def get_unique_item_types(self) -> int:
        """
        Calculates and returns the count of unique item types in the inventory.
        """
        return len(self.inventory.keys())

    def sort_by_quantity(self, item: tuple[str, int]) -> int:
        return item[1]

    def generate_detailed_report(self) -> None:
        """
        Generates and prints a detailed report, sorted by quantity.
        """
        total_items = self.get_total_items()

        if not self.inventory:
            print("Inventory is empty.")
            return

        sorted_inventory: list[tuple[str, int]] = sorted(
            self.inventory.items(), key=self.sort_by_quantity, reverse=True
        )

        print("\n--- Detailed Inventory Report ---")
        print(f"Total items: {total_items}")
        print(f"Unique item types: {self.get_unique_item_types()}\n")
        print(f"{'Item':<15} {'Quantity':<10} {'Percentage':<12}")
        print(f"{'':-<15} {'':-<10} {'':-<12}")

        for item, quantity in sorted_inventory:
            percentage: float = (quantity / total_items) * 100
            print(f"{item:<15} {quantity:<10} {percentage: <10.2f}%")
        print("\n--------------------------------------\n")

    def get_item_quantity(self, item: tuple[str, int]) -> int:
        return item[1]

    def get_abundance_info(self) -> None:
        """
        Determines and displays the most and least abundant item(s).
        """
        if not self.inventory:
            print("Inventory is empty. Cannot determine abundance.")
            return

        most_abundant_item = max(
            self.inventory.items(), key=self.get_item_quantity
        )
        least_abundant_item = min(
            self.inventory.items(), key=self.get_item_quantity
        )

        print("\n--- Abundance Information ---")
        print(
            f"Most abundant item: {most_abundant_item[0]} "
            f"(Quantity: {most_abundant_item[1]})"
        )
        print(
            f"Least abundant item: {least_abundant_item[0]} "
            f"(Quantity: {least_abundant_item[1]})"
        )
        print("\n----------------------------\n")

    def categorize_items_by_abundance(self) -> None:
        """Categorizes items into 'Moderate' and 'Scarce' groups."""
        if not self.inventory:
            print("Inventory is empty. Cannot categorize items.")
            return

        categorized_inventory: dict[str, dict[str, int]] = {
            "Moderate": {},
            "Scarce": {},
        }

        if len(self.inventory) > 0:
            most_abundant_item_name, most_abundant_qty = max(
                self.inventory.items(), key=self.get_item_quantity
            )

            categorized_inventory["Moderate"][most_abundant_item_name] = (
                most_abundant_qty
            )

            for item, quantity in self.inventory.items():
                if item != most_abundant_item_name:
                    categorized_inventory["Scarce"][item] = quantity

        print("\n--- Categorization Report ---")
        print("Categorized Inventory:")
        for category, items in categorized_inventory.items():
            print(f"  {category}:")
            if items:
                for item, qty in items.items():
                    print(f"    - {item}: {qty}")
            else:
                print("    (None)")
        print("-----------------------------")

    def get_restock_suggestions(self) -> None:
        """
        Identifies and suggests items that need restocking (quantity of 1).
        """
        restock_items: list[str] = []
        for item, quantity in self.inventory.items():
            if quantity == 1:
                restock_items += [item]

        print("\n--- Restocking Suggestions ---")
        if restock_items:
            print("The following items need restocking:")
            for item in restock_items:
                print(f"- {item}")
        else:
            print("No items currently need restocking.")
        print("------------------------------")

    def demonstrate_dict_operations(self) -> None:
        """
        Demonstrates various dictionary operations (keys, values, in, get).
        """
        print("\n--- Dictionary Operations Demonstration ---")

        print("Item Names (keys):", list(self.inventory.keys()))
        print("Item Quantities (values):", list(self.inventory.values()))

        known_item = (
            "sword"
            if "sword" in self.inventory
            else next(iter(self.inventory.keys()))
            if len(self.inventory) > 0
            else "test_item_A"
        )
        unknown_item = (
            "elixir" if "elixir" not in self.inventory else "test_item_B"
        )
        print(
            f"Is '{known_item}' in inventory? {known_item in self.inventory}"
        )
        print(
            f"Is '{unknown_item}' in inventory? "
            f"{unknown_item in self.inventory}"
        )
        known_item_get = (
            "potion"
            if "potion" in self.inventory
            else next(iter(self.inventory.keys()))
            if len(self.inventory) > 0
            else "test_item_C"
        )
        unknown_item_get = (
            "scroll" if "scroll" not in self.inventory else "test_item_D"
        )
        print(
            f"Quantity of '{known_item_get}': "
            f"{self.inventory.get(known_item_get)}"
        )
        print(
            f"Quantity of '{unknown_item_get}': "
            f"{self.inventory.get(unknown_item_get, 0)}"
        )
        print("-------------------------------------------")


if __name__ == "__main__":
    initial_inventory_data = {}
    for arg in sys.argv[1:]:
        try:
            item, quantity_str = arg.split(":")
            quantity: int = int(quantity_str)
            initial_inventory_data[item] = quantity
        except ValueError:
            print(
                f"Warning: Skipping invalid argument format: "
                f"{arg}. Expected 'item:quantity'."
            )
        except IndexError:
            print(
                f"Warning: Skipping invalid argument format: "
                f"{arg}. Expected 'item:quantity'."
            )

    if not initial_inventory_data:
        print(
            "No valid inventory items provided via command line. "
            "Using a default sample inventory for demonstration."
        )
        initial_inventory_data = {
            "sword": 1,
            "potion": 5,
            "shield": 2,
            "arrow": 10,
            "coin": 1,
            "gem": 5,
        }

    inventory_system = InventoryMaster(initial_inventory_data)

    inventory_system.generate_detailed_report()
    inventory_system.get_abundance_info()
    inventory_system.categorize_items_by_abundance()
    inventory_system.get_restock_suggestions()
    inventory_system.demonstrate_dict_operations()
