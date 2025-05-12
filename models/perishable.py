from models.item import Item

class PerishableItem(Item):
    """
    A subclass of Item that includes an expiry date for items that expire.
    """
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date  # format: YYYY-MM-DD

    def get_info(self):
        # Adds expiry date to base item info
        base_info = super().get_info()
        return f"{base_info}, Expiry Date: {self.expiry_date}"