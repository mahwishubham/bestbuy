from promotions import Promotion, PercentageDiscountPromotion, SecondHalfPricePromotion, BuyTwoGetOneFreePromotion

class Product:
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

        Raises:
            ValueError: If name is empty or if price or quantity is negative.
        """
        try:
            if not name:
                raise ValueError("Name cannot be empty")
            if price < 0 or quantity < 0:
                raise ValueError("Price and quantity cannot be negative")

            self.name = name
            self.price = price
            self.quantity = quantity
            self.active_status = True  # changed attribute name to avoid method hiding
            self.promotion = None  # No promotion at first
        except Exception as e:
            print(f"Error in initializing product: {e}")
            return None


    def get_quantity(self) -> float:
        """
        Getter function for quantity.
        Returns the quantity (float).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Getter function for active_status.
        Returns True if the product is active, otherwise False.
        """
        return self.active_status

    def activate(self):
        """
        Activates the product.
        """
        self.active_status = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active_status = False

    #  PROMOTION CODE
    def get_promotion(self):
        """
        Getter function for promotion.
        """
        return self.promotion

    def set_promotion(self, promotion):
        """
        Setter function for promotion.
        """
        self.promotion = promotion

    def show(self) -> str:
        """
        Returns a string that represents the product, for example:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        promotion_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_text}"


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if not self.is_active():
            raise Exception("Product is not active")

        if self.quantity < quantity:
            raise Exception("Insufficient quantity")

        self.quantity -= quantity
        price = self.price * quantity
        if self.promotion:
            price = self.promotion.apply_promotion(self, quantity)
        return price

class NonStockedProduct(Product):
    """
    NonStockedProduct class represents a non-stocked product which always has zero quantity.
    """
    def __init__(self, name, price):
        """
        Initializes a NonStockedProduct instance.
        The quantity is always zero.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """
        Overrides the setter function for quantity.
        For NonStockedProduct, quantity is always zero and cannot be changed.
        """
        raise NotImplementedError("Quantity cannot be changed for NonStockedProduct")

    def buy(self, quantity=1):
        """
        Overrides the buy function. Always available to buy.
        """
        return self.price * quantity

    def show(self):
        """
        Overrides the show function to show the special characteristics of NonStockedProduct.
        """
        return f"{self.name}, Price: {self.price}, Non-stocked product"

class LimitedProduct(Product):
    """
    LimitedProduct class represents a limited product that can be purchased limited number of times.
    """
    def __init__(self, name, price, quantity, max_purchase):
        """
        Initializes a LimitedProduct instance.

        Args:
            max_purchase (int): The maximum quantity that can be purchased at a time.
        """
        super().__init__(name, price, quantity)
        self.max_purchase = max_purchase

    def buy(self, quantity):
        """
        Overrides the buy function.
        The quantity to be purchased cannot exceed max_purchase.
        """
        if quantity > self.max_purchase:
            raise Exception(f"Cannot purchase more than {self.max_purchase} at a time")
        else:
            return super().buy(quantity)

    def show(self):
        """
        Overrides the show function to show the special characteristics of LimitedProduct.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max purchase: {self.max_purchase}"


if __name__ == '__main__':
    try:
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        print(bose.buy(50))
        print(mac.buy(100))
        print(mac.is_active())

        print(bose.show())
        print(mac.show())

        bose.set_quantity(1000)
        print(bose.show())
    except Exception as e:
        print(f"An error occurred: {e}")