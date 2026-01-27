#!/usr/bin/env python3

import sys


class InventoryMaster:
    def __init__(
        self, initial_inventory: dict[str, int] | None = None
    ) -> None:
        self.inventory: dict[str, int] = {}
        if initial_inventory:
            self.inventory.update(initial_inventory)

    def get_total_items(self):
        """Calculates and returns the total number of all items in the inventory."""
        return sum(self.inventory.values())

    def get_unique_item_types(self):
        """Calculates and returns the count of unique item types in the inventory."""
        return len(self.inventory.keys())

    def generate_detailed_report(self):
        """Generates and prints a detailed report of the inventory, sorted by quantity."""
        total_items = self.get_total_items()

        if not self.inventory:
            print("Inventory is empty.")
            return

        # Sort items by quantity in descending order
        sorted_inventory = sorted(
            self.inventory.items(), key=lambda item: item[1], reverse=True
        )

        print("\n--- Detailed Inventory Report ---")
        print(f"Total items: {total_items}")
        print(f"Unique item types: {self.get_unique_item_types()}\n")
        print(f"{'Item':<15} {'Quantity':<10} {'Percentage':<12}")
        print(f"{'':-<15} {'':-<10} {'':-<12}")

        for item, quantity in sorted_inventory:
            percentage = (quantity / total_items) * 100
            print(f"{item:<15} {quantity:<10} {percentage: <10.2f}%")
        print("-----------------------------------")

    def get_abundance_info(self) -> None:
        """
        Determines and displays the most and least abundant item(s).
        """
        if not self.inventory:
            print("Inventory is empty. Cannot determine abundance.")
            return

        # Find the most abundant item
        most_abundant_item = max(
            self.inventory.items(), key=lambda item: item[1]
        )
        # Find the least abundant item
        least_abundant_item = min(
            self.inventory.items(), key=lambda item: item[1]
        )

        print("\n--- Abundance Information ---")
        print(
            f"Most abundant item: {most_abundant_item[0]} (Quantity: {
                most_abundant_item[1]
            })"
        )
        print(
            f"Least abundant item: {least_abundant_item[0]} (Quantity: {
                least_abundant_item[1]
            })"
        )
        print("----------------------------")

    def categorize_items_by_abundance(self) -> None:
        """
        Categorizes items into 'Moderate' (most abundant) and 'Scarce' groups.
        """
        if not self.inventory:
            print("Inventory is empty. Cannot categorize items.")
            return

        categorized_inventory = {"Moderate": {}, "Scarce": {}}

        # Determine the most abundant item
        if len(self.inventory) > 0:
            most_abundant_item_name, most_abundant_qty = max(
                self.inventory.items(), key=lambda item: item[1]
            )

            # Add the most abundant item to 'Moderate'
            categorized_inventory["Moderate"][most_abundant_item_name] = (
                most_abundant_qty
            )

            # Add all other items to 'Scarce'
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
        """Identifies and suggests items that need restocking (quantity of 1)."""
        restock_items = []
        for item, quantity in self.inventory.items():
            if quantity == 1:
                restock_items.append(item)

        print("\n--- Restocking Suggestions ---")
        if restock_items:
            print("The following items need restocking:")
            for item in restock_items:
                print(f"- {item}")
        else:
            print("No items currently need restocking.")
        print("------------------------------")

    def demonstrate_dict_operations(self) -> None:
        """Demonstrates various dictionary operations (keys, values, in, get)."""
        print("\n--- Dictionary Operations Demonstration ---")

        # 1. Display all item names (keys)
        print("Item Names (keys):", list(self.inventory.keys()))

        # 2. Display all item quantities (values)
        print("Item Quantities (values):", list(self.inventory.values()))

        # 3. Demonstrate 'in' operator for known and unknown items
        known_item = (
            "sword"
            if "sword" in self.inventory
            else list(self.inventory.keys())[0]
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
            f"Is '{unknown_item}' in inventory? {
                unknown_item in self.inventory
            }"
        )

        # 4. Demonstrate get() method for known and unknown items with default value
        known_item_get = (
            "potion"
            if "potion" in self.inventory
            else list(self.inventory.keys())[0]
            if len(self.inventory) > 0
            else "test_item_C"
        )
        unknown_item_get = (
            "scroll" if "scroll" not in self.inventory else "test_item_D"
        )
        print(
            f"Quantity of '{known_item_get}': {
                self.inventory.get(known_item_get)
            }"
        )
        print(
            f"Quantity of '{unknown_item_get}' (with default 0): {
                self.inventory.get(unknown_item_get, 0)
            }"
        )
        print("-------------------------------------------")


if __name__ == "__main__":
    initial_inventory_data = {}
    for arg in sys.argv[1:]:
        try:
            item, quantity_str = arg.split(":")
            quantity = int(quantity_str)
            initial_inventory_data[item] = quantity
        except ValueError:
            print(
                f"Warning: Skipping invalid argument format: {
                    arg
                }. Expected 'item:quantity'."
            )
        except IndexError:
            print(
                f"Warning: Skipping invalid argument format: {
                    arg
                }. Expected 'item:quantity'."
            )

    if not initial_inventory_data:
        print(
            "No valid inventory items provided via command line. Using a default sample inventory for demonstration."
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
"""
=== Inventory System Analysis ===
Total items in inventory: 12
Unique item types: 5
=== Current Inventory ===
potion: 5 units (41.7%)
armor: 3 units (25.0%)
shield: 2 units (16.7%)
sword: 1 unit (8.3%)
helmet: 1 unit (8.3%)
=== Inventory Statistics ===
Most abundant: potion (5 units)
Least abundant: sword (1 unit)
=== Item Categories ===
Moderate: {'potion': 5}
Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}
=== Management Suggestions ===
Restock needed: ['sword', 'helmet']
=== Dictionary Properties Demo ===
Dictionary keys: ['sword', 'potion', 'shield', 'armor', 'helmet']
Dictionary values: [1, 5, 2, 3, 1]
Sample lookup - 'sword' in inventory: True
"""
