# Imports if we need some
# -
# - 
# Product class (as soon as we learn about classes)
# -
# -


def create_product(name, price, quantity, category, **kwargs):
    """Here we create a new Product as dict"""
    product = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category,
        "additional_attributes": kwargs
    }
    return product

def update_quantity(product, amount):
    