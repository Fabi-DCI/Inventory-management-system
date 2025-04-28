Inventory Management System


Description

This project is an Inventory Management System built using Python. It helps users to efficiently manage and track their products, with functionalities like adding, removing, updating, and viewing inventory items. The system also provides the ability to search and view product details and calculates the total inventory value.
Features

    Add Products: Add new products to the inventory.

    Remove Products: Remove existing products from the inventory.

    Update Product Information: Update details like quantity or price of products.

    View Product Details: Retrieve information on any product in the inventory.

    Total Inventory Value: Calculate the total value of all items in the inventory.

    Search by Name: Search products by name for detailed information.

Technologies Used

    Python 3.x - The project is built using Python as the primary programming language.

Installation
Prerequisites

    Python 3.x installed on your machine.

Setup

    Clone the repository:

git clone git@github.com:Fabi-DCI/Inventory-management-system.git

Navigate to the project directory:

cd Inventory-management-system

(Optional) Install any necessary dependencies if you have a requirements.txt file:

pip install -r requirements.txt

Run the application:

    python main.py

Usage

    Add products to the inventory by creating Product instances and adding them via the add_product() method.

    Update the quantity of a product using the update_product_quantity() method.

    Remove products using the remove_product() method by specifying the product name.

    Get product information using get_product_info() with the product's name.

    Calculate the total inventory value using get_total_inventory_value().

Example usage in main.py:

# Create product instances
apple = Product("Apple", 0.50, 200, "Fruit")
milk = Product("Milk", 1.50, 50, "Dairy")

# Add products to inventory
inventory.add_product(apple)
inventory.add_product(milk)

# Get product information
print(inventory.get_product_info("Apple"))

Unit Tests

The project includes unit tests to verify the functionality of the InventoryManager class and Product class.
Run Unit Tests:

python -m unittest test_inventory.py

This will execute the test cases defined in the test_inventory.py file.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Notes:

    This project doesn’t rely on any database. All inventory data is stored in memory (in Python objects).

    The system works with a simple CLI interface.