class Item:
    """
    Represents a regular inventory item with:
    - name: item's name
    - price: cost per unit (in PKR)
    - quantity: how many units available
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_info(self):
        # Returns a formatted string with item details
        return f"Name: {self.name}, Price: {self.price:.2f} PKR, Quantity: {self.quantity}"

    def get_value(self):
        # Calculates total value of this item (price * quantity)
        return self.price * self.quantity