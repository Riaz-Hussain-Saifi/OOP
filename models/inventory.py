# Manages a collection of items
class Inventory:
    def __init__(self):
        self.items = []

    # Add new item to inventory
    def add_item(self, item):
        self.items.append(item)

    # Remove item by name
    def remove_item(self, name):
        self.items = [item for item in self.items if item.get_name() != name]

    # Show all items
    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print(item.get_info())

    # Total value of all items
    def total_inventory_value(self):
        return sum(item.calculate_value() for item in self.items)
