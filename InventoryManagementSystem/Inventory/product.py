class Product:
    def __init__(self, name, price, quantity, category):
        """
        Initializes a Product instance.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_quantity(self, new_quantity):
        """
        Updates the quantity of the product.
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

    def update_price(self, new_price):
        """
        Updates the price of the product.
        """
        if new_price >= 0:
            self.price = new_price
        else:
            print("Price cannot be negative.")

    def get_product_info(self):
        """
        Retrieves product details as a formatted string.
        """
        return f"Product Name: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def get_total_value(self):
        """
        Calculates and returns the total value of the product in stock.
        """
        return self.price * self.quantity