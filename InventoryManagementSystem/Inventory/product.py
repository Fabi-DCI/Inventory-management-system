# Imports if we need some
# -
# - 

class Product:
    def __init__(self, name, price, quantity, category):   #country, supplier 
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        #self.supplier = supplier (maybe we can give our products a supplier where they come from etc)
        #self.import_country = country (same for supplier) but then we have to add them behind our products below !!just an idea!!

# Fruits & Vegetables
Apple = Product("Apple", "$0.50", 200, "Fruit")
Banana = Product("Banana", "$0.30", 150, "Fruit")
Carrot = Product("Carrot", "$0.40", 180, "Vegetable")
Broccoli = Product("Broccoli", "$1.20", 100, "Vegetable")
Tomato = Product("Tomato", "$0.80", 250, "Vegetable")
Potato = Product("Potato", "$0.60", 300, "Vegetable")
Spinach = Product("Spinach", "$1.50", 90, "Vegetable")
Onion = Product("Onion", "$0.70", 220, "Vegetable")
Bell_Pepper = Product("Bell Pepper", "$1.00", 130, "Vegetable")
Cucumber = Product("Cucumber", "$0.50", 140, "Vegetable")

# Dairy Products
Milk = Product("Milk", "$1.50", 50, "Dairy")
Cheese = Product("Cheese", "$3.00", 40, "Dairy")
Yogurt = Product("Yogurt", "$0.90", 100, "Dairy")
Butter = Product("Butter", "$2.50", 30, "Dairy")
Cream = Product("Cream", "$1.80", 60, "Dairy")

# Beverages
Orange_Juice = Product("Orange Juice", "$2.00", 80, "Beverage")
Soda = Product("Soda", "$1.20", 150, "Beverage")
Bottled_Water = Product("Bottled Water", "$0.50", 300, "Beverage")
Tea_Bags = Product("Tea Bags", "$3.50", 70, "Beverage")
Coffee = Product("Coffee", "$5.00", 40, "Beverage")

# Bakery
Bread = Product("Bread", "$1.20", 60, "Bakery")
Croissant = Product("Croissant", "$2.00", 30, "Bakery")
Bagels = Product("Bagels", "$1.80", 50, "Bakery")
Muffins = Product("Muffins", "$1.50", 40, "Bakery")
Donuts = Product("Donuts", "$1.00", 100, "Bakery")

# Meat & Seafood
Chicken_Breast = Product("Chicken Breast", "$5.00", 20, "Meat")
Ground_Beef = Product("Ground Beef", "$6.50", 25, "Meat")
Salmon_Fillet = Product("Salmon Fillet", "$8.00", 15, "Seafood")
Shrimp = Product("Shrimp", "$10.00", 10, "Seafood")
Pork_Chops = Product("Pork Chops", "$7.00", 18, "Meat")

# Snacks
Potato_Chips = Product("Potato Chips", "$1.50", 120, "Snack")
Chocolate_Bar = Product("Chocolate Bar", "$0.80", 200, "Snack")
Popcorn = Product("Popcorn", "$1.20", 100, "Snack")
Cookies = Product("Cookies", "$2.00", 80, "Snack")
Granola_Bars = Product("Granola Bars", "$3.00", 60, "Snack")

# Household Items
Toilet_Paper = Product("Toilet Paper (pack)", "$5.00", 40, "Household")
Dish_Soap = Product("Dish Soap", "$2.50", 70, "Household")
Laundry_Detergent = Product("Laundry Detergent", "$10.00", 20, "Household")
Paper_Towels = Product("Paper Towels (roll)", "$3.00", 50, "Household")
Trash_Bags = Product("Trash Bags (box)", "$4.00", 30, "Household")

# Frozen Foods
Frozen_Pizza = Product("Frozen Pizza", "$5.00", 20, "Frozen Food")
Ice_Cream = Product("Ice Cream", "$3.50", 40, "Frozen Food")
Frozen_Vegetables = Product("Frozen Vegetables", "$2.50", 60, "Frozen Food")
Chicken_Nuggets = Product("Chicken Nuggets", "$4.50", 30, "Frozen Food")
Fish_Sticks = Product("Fish Sticks", "$4.00", 25, "Frozen Food")


 def get_product_info(self):
        """
        Returns a string representation of the product's details.
        """
        info = f"Product: {self.name}\n" \
               f"Price: ${self.price}\n" \
               f"Quantity: {self.quantity}\n" \
               f"Category: {self.category}\n"
        return 
       #if self.description:      if we choose to give some a supplier/country
       #    info += f"Description: {self.description}\n"
       #if self.supplier:
       #    info += f"Supplier: {self.supplier}\n"
       #if self.country:
       #    info += f":Country: {self.country}\n"
       #  return info
