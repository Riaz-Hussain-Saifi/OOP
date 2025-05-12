from models.perishable import PerishableItem

class Inventory:
    """
    Manages the inventory:
    - Adds or updates items
    - Removes items
    - Calculates total value
    """
    def __init__(self):
        self.items = []  # List to hold all inventory items

    def find_item(self, item_name):
        # Search for an item by name
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def add_item(self, new_item):
        # Add new item or update existing one
        existing_item = self.find_item(new_item.name)
        if existing_item:
            # Update quantity and price
            existing_item.quantity += new_item.quantity
            existing_item.price = new_item.price
            # Update expiry if it's a perishable item
            if isinstance(new_item, PerishableItem) and hasattr(existing_item, 'expiry_date'):
                existing_item.expiry_date = new_item.expiry_date
            return "updated"
        else:
            self.items.append(new_item)
            return "added"

    def remove_item(self, item_name):
        # Remove item from inventory by name
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            return True
        return False

    def get_total_value(self):
        # Total monetary value of all inventory items
        return sum(item.get_value() for item in self.items)
