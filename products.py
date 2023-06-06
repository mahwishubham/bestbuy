from abc import ABC
from promotions import Promotion, PercentageDiscountPromotion, SecondHalfPricePromotion, BuyTwoGetOneFreePromotion


class Product(ABC):
    """
    Product class represents a product with name, price, quantity, and status.
    """
    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active_status = True
        self._promotion = None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        if not issubclass(type(value), Promotion):
            raise ValueError("Value should be an instance of Promotion or its subclass")
        self._promotion = value

    @property
    def is_active(self):
        return self._active_status

    def activate(self):
        self._active_status = True

    def deactivate(self):
        self._active_status = False

    def __str__(self):
        promotion_text = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{promotion_text}"

    def __gt__(self, other):
        return self._price > other._price

    def __lt__(self, other):
        return self._price < other._price

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if not self.is_active:
            raise Exception("Product is not active")

        if self._quantity < quantity:
            raise Exception("Insufficient quantity")

        self._quantity -= quantity
        price = self._price * quantity
        if self._promotion:
            price = self._promotion.apply_promotion(self, quantity)
        return price


class NonStockedProduct(Product):
    """
    NonStockedProduct class represents a non-stocked product which always has zero quantity.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def __str__(self):
        return super().__str__() + ", Non-stocked product"

    def buy(self, quantity=1):
        return self._price * quantity


class LimitedProduct(Product):
    """
    LimitedProduct class represents a limited product that can be purchased limited number of times.
    """
    def __init__(self, name, price, quantity, max_purchase):
        super().__init__(name, price, quantity)
        self._max_purchase = max_purchase

    def __str__(self):
        return super().__str__() + f", Max purchase: {self._max_purchase}"

    def buy(self, quantity):
        if quantity > self._max_purchase:
            raise Exception(f"Cannot purchase more than {self._max_purchase} at a time")
        else:
            return super().buy(quantity)


if __name__ == '__main__':
    try:
        # setup initial stock of inventory
        mac =  products.Product("MacBook Air M2", price=1450, quantity=100)
        bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        pixel = products.Product("Google Pixel 7", price=500, quantity=250, maximum=1)

        best_buy = store.Store([mac, bose])
        mac.price = -100         # Should give error
        print(mac)               # Should print `MacBook Air M2, Price: $1450 Quantity:100`
        print(mac > bose)        # Should print True
        print(mac in best_buy)   # Should print True
        print(pixel in best_buy) # Should print False
    except Exception as e:
        print(f"An error occurred: {e}")
