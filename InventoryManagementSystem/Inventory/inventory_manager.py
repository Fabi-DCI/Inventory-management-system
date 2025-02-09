from product import Product

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        """Add a new product to the inventory."""
        if product.name in self.inventory:
            print(f"{product.name} already exists. Updating quantity instead.")
            self.inventory[product.name].update_quantity(self.inventory[product.name].quantity + product.quantity)
        else:
            self.inventory[product.name] = product

    def remove_product(self, product_name):
        """Remove a product from inventory."""
        if product_name in self.inventory:
            del self.inventory[product_name]
            print(f"{product_name} has been removed from inventory.")
        else:
            print(f"{product_name} not found in inventory.")

    def update_product_quantity(self, product_name, new_quantity):
        """Update the quantity of a specific product."""
        if product_name in self.inventory:
            self.inventory[product_name].update_quantity(new_quantity)
        else:
            print(f"{product_name} not found in inventory.")

    def get_product_info(self, product_name):
        """Retrieve information about a specific product."""
        if product_name in self.inventory:
            return self.inventory[product_name].get_product_info()
        else:
            return "Product not found."

    def get_total_inventory_value(self):
        """Calculate the total value of all products in inventory."""
        return sum(product.get_total_value() for product in self.inventory.values())

if __name__ == "__main__":
    print("Inventory Manager module loaded.")




