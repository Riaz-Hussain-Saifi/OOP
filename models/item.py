# Class representing a generic inventory item
class Item:
    def __init__(self, name, price, quantity):
        # Encapsulated (private) variables
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Public method to display item info
    def get_info(self):
        return f"Item: {self.__name}, Price: {self.__price} PKR, Quantity: {self.__quantity}"

    # Method to update quantity
    def update_quantity(self, quantity):
        self.__quantity += quantity

    # Calculate total value (price × quantity)
    def calculate_value(self):
        return self.__price * self.__quantity

    # Getter methods to safely access private data
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity
