"""Module for defining product-related classes and their functionalities."""

from abc import ABC
from promotions import Promotion

class Product(ABC):
    """Represents a product with name, price, quantity, and status."""
    def __init__(self, product_id, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")

        self._id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active_status = True
        self._promotion = None

    @property
    def quantity(self):
        """Returns the quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Sets the quantity of the product and deactivates it if the quantity is 0."""
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    @property
    def name(self):
        """Returns the name of the product."""
        return self._name

    @property
    def product_id(self):
        """Returns the id of the product."""
        return self._id

    @property
    def price(self):
        """Returns the price of the product."""
        return self._price

    @property
    def promotion(self):
        """Returns the promotion applied to the product."""
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        """Sets a promotion for the product if it's an instance of Promotion or its subclass."""
        if not isinstance(value, Promotion):
            raise ValueError("Value should be an instance of Promotion or its subclass")
        self._promotion = value

    @property
    def is_active(self):
        """Checks if the product is active."""
        return self._active_status

    def activate(self):
        """Activates the product."""
        self._active_status = True

    def deactivate(self):
        """Deactivates the product."""
        self._active_status = False

    def __str__(self):
        promotion_text = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{promotion_text}"

    def __gt__(self, other):
        """Enables comparison of products based on price (greater than)."""
        return self._price > other._price

    def __lt__(self, other):
        """Enables comparison of products based on price (less than)."""
        return self._price < other._price

    def buy(self, quantity):
        """Processes the purchase of the product, applying any promotions."""
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if not self.is_active:
            raise ValueError("Product is not active")

        if self._quantity < quantity:
            raise ValueError("Insufficient quantity")

        self._quantity -= quantity
        price = self._price * quantity
        if self._promotion:
            price = self._promotion.apply_promotion(self, quantity)
        return price


class NonStockedProduct(Product):
    """Represents a non-stocked product which always has zero quantity."""
    def __init__(self, product_id, name, price):
        super().__init__(product_id, name, price, quantity=0)

    def __str__(self):
        return super().__str__() + ", Non-stocked product"

    def buy(self, quantity=1):
        """Processes the purchase of a non-stocked product."""
        return self._price * quantity


class LimitedProduct(Product):
    """Represents a limited product that can be purchased a limited number of times."""
    def __init__(self, product_id, name, price, quantity, max_purchase):
        super().__init__(product_id, name, price, quantity)
        self._max_purchase = max_purchase

    def __str__(self):
        return super().__str__() + f", Max purchase: {self._max_purchase}"

    def buy(self, quantity):
        """
        Processes the purchase of a limited product, 
        ensuring it doesn't exceed the max purchase limit.
        """
        if quantity > self._max_purchase:
            raise ValueError(f"Cannot purchase more than {self._max_purchase} at a time")
        return super().buy(quantity)
