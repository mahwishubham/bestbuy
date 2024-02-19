import pytest
from products import Product


def test_product_creation():
    """
    Test that creating a normal product works.
    """
    product = Product(product_id='101', name="Bose QuietComfort Earbuds", price=250, quantity=500)
    assert product.name == "Bose QuietComfort Earbuds"
    assert product.price == 250
    assert product.quantity == 500


def test_invalid_product_creation():
    """
    Test that creating a product with invalid details (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError):
        Product(product_id='101', name="", price=250, quantity=500)
    with pytest.raises(ValueError):
        Product(product_id='101', name="Bose QuietComfort Earbuds", price=-250, quantity=500)
    with pytest.raises(ValueError):
        Product(product_id='101', name="Bose QuietComfort Earbuds", price=250, quantity=-500)


def test_product_deactivation():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    """
    product = Product(product_id='101', name="Bose QuietComfort Earbuds", price=250, quantity=500)
    product.quantity = 0
    assert not product.is_active


def test_product_purchase():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    product = Product(product_id='101', name="Bose QuietComfort Earbuds", price=250, quantity=500)
    total_price = product.buy(50)
    assert product.quantity == 450
    assert total_price == 250 * 50


def test_insufficient_quantity_purchase():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    product = Product(product_id="101",name="Bose QuietComfort Earbuds", price=250, quantity=500)
    with pytest.raises(Exception):
        product.buy(600)
