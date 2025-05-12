from models.item import Item
from models.perishable import PerishableItem
from models.inventory import Inventory
from datetime import datetime

class MainApp:
    """
    CLI (Command Line Interface) for managing the inventory through terminal input.
    """
    def __init__(self):
        # Initialize the inventory system
        self.inventory = Inventory()

    def run(self):
        # Main menu loop for user interaction
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
                self.view_items()
            elif choice == "5":
                self.view_total_value()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

    def add_item(self):
        # Gather user input for a regular item
        name = input("Enter item name: ")
        price = float(input("Enter price (PKR): "))
        quantity = int(input("Enter quantity: "))
        item = Item(name, price, quantity)
        self.inventory.add_item(item)
        print("Item added or updated.")

    def add_perishable_item(self):
        # Gather user input for a perishable item with expiry date
        name = input("Enter item name: ")
        price = float(input("Enter price (PKR): "))
        quantity = int(input("Enter quantity: "))
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        try:
            # Validate date format
            datetime.strptime(expiry, "%Y-%m-%d")
            p_item = PerishableItem(name, price, quantity, expiry)
            self.inventory.add_item(p_item)
            print("Perishable item added or updated.")
        except ValueError:
            print("Invalid date format.")

    def remove_item(self):
        # Ask user which item to remove
        name = input("Enter item name to remove: ")
        if self.inventory.remove_item(name):
            print("Item removed.")
        else:
            print("Item not found.")

    def view_items(self):
        # Display all items in inventory
        for item in self.inventory.items:
            print(item.get_info())

    def view_total_value(self):
        # Display total monetary value of inventory
        total = self.inventory.get_total_value()
        print(f"Total Inventory Value: {total:.2f} PKR")