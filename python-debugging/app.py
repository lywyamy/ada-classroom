from grocery_store.product import create_product
from grocery_store.order import create_order, calculate_total, add_product


kamala_order = create_order([], "Kamala")

product_1 = create_product("Apples", 3.47)
product_2 = create_product("Oranges", 4.89)
product_3 = create_product("Macbook", 1379.99)

add_product(kamala_order, product_1)
add_product(kamala_order, product_2)
add_product(kamala_order, product_3)

print(f"The order total for {kamala_order['customer_name']} is " +
    f"{calculate_total(kamala_order)}")

