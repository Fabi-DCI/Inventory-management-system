class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

    def update_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Price cannot be negative.")

    def get_product_info(self):
        return f"Product Name: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def get_total_value(self):
        return self.price * self.quantity

def main():
    apple = Product("Apple", 0.50, 200, "Fruit")
    banana = Product("Banana", 0.30, 150, "Fruit")
    carrot = Product("Carrot", 0.40, 180, "Vegetable")

    print(apple.get_product_info())
    print(f"Total Value of Apple: ${apple.get_total_value():.2f}")
    
    apple.update_price(0.55)
    apple.update_quantity(250)

    print(apple.get_product_info())
    print(f"Total Value of Apple: ${apple.get_total_value():.2f}")

if __name__ == "__main__":
    main()





