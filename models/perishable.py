from models.item import Item

# Inherited class for items that expire
class PerishableItem(Item):
    def __init__(self, name, price, quantity, expiry_date):
        # Inherit base properties
        super().__init__(name, price, quantity)
        self.__expiry_date = expiry_date

    # Overriding method for polymorphism
    def get_info(self):
        return f"{super().get_info()}, Expiry Date: {self.__expiry_date}"
