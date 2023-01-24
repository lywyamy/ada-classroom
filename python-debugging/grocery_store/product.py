
def create_product(name, price):
    return {
        "name": name,
        "price": price,
    }

def print_product(product):
    return f"{product['name']} - ${product['price']}"
    

