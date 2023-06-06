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

    def show(self) -> str:
        """
        Returns a string that represents the product, for example:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

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
        return self.price * quantity


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