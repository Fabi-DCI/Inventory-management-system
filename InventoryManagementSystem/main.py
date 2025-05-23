from Inventory.product import Product
from Inventory.inventory_manager import InventoryManager

def main():
    inventory = InventoryManager()

    apple = Product("Apple", 0.50, 200, "Fruit")
    milk = Product("Milk", 1.50, 50, "Dairy")
    bread = Product("Bread", 1.20, 60, "Bakery")

    inventory.add_product(apple)
    inventory.add_product(milk)
    inventory.add_product(bread)

    print(inventory.get_product_info("Apple"))
    print(inventory.get_product_info("Milk"))

    inventory.update_product_quantity("Milk", 100)

    print(f"Total Inventory Value: ${inventory.get_total_inventory_value():.2f}")

if __name__ == "__main__":
    main()
