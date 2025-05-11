from models.item import Item
from models.perishable import PerishableItem
from models.inventory import Inventory
from datetime import datetime

# Runs the menu system
class MainApp:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
            print("1. Add Item")
            print("2. Add Perishable Item")
            print("3. Remove Item")
            print("4. Show All Items")
            print("5. Show Total Inventory Value")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.add_perishable_item()
            elif choice == "3":
                self.remove_item()
            elif choice == "4":
                self.inventory.list_items()
            elif choice == "5":
                print("Total Inventory Value:", self.inventory.total_inventory_value(), "PKR")
            elif choice == "6":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

    # Option 1: Add Item
    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter price (PKR): "))
        quantity = int(input("Enter quantity: "))
        item = Item(name, price, quantity)
        self.inventory.add_item(item)
        print("Item added successfully.")

    # Option 2: Add Perishable Item
    def add_perishable_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter price (PKR): "))
        quantity = int(input("Enter quantity: "))
        expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
        try:
            datetime.strptime(expiry_date, "%Y-%m-%d")
            p_item = PerishableItem(name, price, quantity, expiry_date)
            self.inventory.add_item(p_item)
            print("Perishable item added successfully.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Option 3: Remove Item
    def remove_item(self):
        name = input("Enter item name to remove: ")
        self.inventory.remove_item(name)
        print("Item removed (if it existed).")
