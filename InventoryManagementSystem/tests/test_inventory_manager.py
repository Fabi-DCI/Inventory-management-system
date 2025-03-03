import unittest
from Inventory.product import Product
from Inventory.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    
    def setUp(self):
        self.inventory_manager = InventoryManager()
        self.product1 = Product("Shoes", 49.99, 10, "Footwear")
        self.product2 = Product("Shirt", 19.99, 20, "Apparel")

    def test_add_product(self):
        self.inventory_manager.add_product(self.product1)
        self.inventory_manager.add_product(self.product2)
        self.assertEqual(len(self.inventory_manager.inventory), 2)

    def test_remove_product(self):
        self.inventory_manager.add_product(self.product1)
        self.inventory_manager.remove_product("Shoes")
        self.assertEqual(len(self.inventory_manager.inventory), 0)

    def test_get_product_info(self):
        self.inventory_manager.add_product(self.product1)
        product_info = self.inventory_manager.get_product_info("Shoes")
        self.assertEqual(product_info, "Product Name: Shoes, Price: 49.99, Quantity: 10")

    def test_update_product_quantity(self):
        self.inventory_manager.add_product(self.product1)
        self.inventory_manager.update_product_quantity("Shoes", 15)
        self.assertEqual(self.product1.quantity, 15)

if __name__ == '__main__':
    unittest.main()










    
