class InventoryManager:
    def __init__(self):
        self.inventory = []  

    def add_product(self, product):
        for p in self.inventory:
            if p.name == product.name: 
                print(f"Product '{product.name}' is already in the inventory.")
                return
        self.inventory.append(product) 

    def remove_product(self, product_name):
        for product in self.inventory:
            if product.name == product_name:  
                self.inventory.remove(product)  
                return
        print(f"Product '{product_name}' not found in the inventory.")  

    def get_product_info(self, product_name):
        for product in self.inventory:
            if product.name == product_name:  
                return product.get_product_info()  
        print(f"Product '{product_name}' not found in the inventory.")  

    def update_product_quantity(self, product_name, new_quantity):
        for product in self.inventory:
            if product.name == product_name:  
                product.update_quantity(new_quantity)  
                return
        print(f"Product '{product_name}' not found in the inventory.")  

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.inventory:  
            total_value += product.price * product.quantity  
        return total_value  












