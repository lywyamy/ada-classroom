import pytest
from grocery_store.order import create_order, calculate_total, add_product
from grocery_store.product import create_product

def test_order_creation():
    # Arrange
    product_one = create_product("Trombone", 478.95)
    product_two = create_product("Guitar", 327.99)
    product_three = create_product("Triangle", 2)
    products = [product_one, product_two, product_three]

    # Act
    sample_order = create_order(products, "Shona Frederick")

    # Assert
    assert len(sample_order["products"]) == 3
    assert sample_order["customer_name"] == "Shona Frederick"
    for product in products:
        assert product in sample_order["products"]

def test_order_creation_with_no_products():
    # Arrange
    products = []

    # Act
    sample_order = create_order(products, "Shona Frederick")

    # Assert
    assert len(sample_order["products"]) == 0
    assert sample_order["customer_name"] == "Shona Frederick"

def test_add_product():
    # Arrange
    product_one = create_product("Trombone", 478.95)
    product_two = create_product("Guitar", 327.99)
    product_three = create_product("Triangle", 2)
    products = [product_one, product_two, product_three]
    sample_order = create_order(products, "Shona Frederick")

    new_product = create_product("Bass", 115)

    # Act
    add_product(sample_order, new_product)

    # Assert
    assert len(sample_order["products"]) == 4
    assert new_product in sample_order["products"]
    
def test_calculate_total_with_no_products():
    # Arrange
    order = create_order([], "Shona Frederick")

    # Act
    total = calculate_total(order)

    # Assert
    assert total == 0

def test_calculate_total_with_multiple_products():
    # Arrange
    product_one = create_product("Trombone", 478.95)
    product_two = create_product("Guitar", 327.99)
    product_three = create_product("Triangle", 2)
    products = [product_one, product_two, product_three]

    order = create_order(products, "Shona Frederick")


    # Act
    total = calculate_total(order)

    # Assert
    assert total == pytest.approx(478.95 + 327.99 + 2) 