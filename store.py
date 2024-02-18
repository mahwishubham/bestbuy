"""
Store.py
"""
from typing import List, Tuple, Union
from products import Product

class Store:
    """
    Store class represents a store with a list of products.
    """
    def __init__(self, products: List[Product] = None):
        """
        Initializes a Store instance with a list of products.

        Args:
            products (List[Product], optional): The list of products in the store. Defaults to None.
        """
        self._products = products if products else []

    @property
    def products(self) -> List[Product]:
        """Returns the list of products in the store."""
        return self._products

    @products.setter
    def products(self, products: List[Product]):
        """
        Sets the list of products in the store.

        Args:
            products (List[Product]): A list of Product instances to be set as the store's products.
        """
        if isinstance(products, list) and all(isinstance(product, Product) for product in products):
            self._products = products
        else:
            raise TypeError("Products should be a list of Product instances")

    def __str__(self) -> str:
        """
        Returns a string representation of all products in the store.
        """
        p = ""
        for product in self._products:
            p += f'{product.product_id}: {str(product)} \n'
        return p

    def __lt__(self, other: 'Store') -> bool:
        """
        Checks if this store's total value is less than another store's total value.

        Args:
            other (Store): Another store to compare with.

        Returns:
            bool: True if this store's total value is less than the other's, False otherwise.
        """
        return self.get_total_value() < other.get_total_value()

    def __gt__(self, other: 'Store') -> bool:
        """
        Checks if this store's total value is greater than another store's total value.

        Args:
            other (Store): Another store to compare with.

        Returns:
            bool: True if this store's total value is greater than the other's, False otherwise.
        """
        return self.get_total_value() > other.get_total_value()

    def __contains__(self, item) -> bool:
        """
        Checks if a product exists in the store by name or ID.

        Args:
            item (str): The product name or ID to check for.

        Returns:
            bool: True if the product exists, False otherwise.
        """
        return any(item in (product.name, product.product_id) for product in self.products)

    def __add__(self, other: 'Store') -> 'Store':
        """
        Adds the products of another store to this store's products and 
        returns a new Store instance.

        Args:
            other (Store): Another store whose products are to be added.

        Returns:
            Store: A new Store instance containing products from both stores.
        """
        return Store(self._products + other.products)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of products.
        """
        return sum(product.quantity for product in self.products)

    def get_total_value(self) -> float:
        """
        Calculates the total value of all products in the store.

        Returns:
            float: The total value of products.
        """
        return sum(product.price * product.quantity for product in self.products)

    def find_product(self, product_name: str) -> Union[Product, None]:
        """
        Finds a product by its name or ID.

        Args:
            product_name (str): The name or ID of the product to find.

        Returns:
            Union[Product, None]: The Product instance if found, None otherwise.
        """
        for product in self.products:
            if product_name in {product.name, product.product_id}:
                return product
        return None

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order based on a shopping list of products and quantities.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples containing
            Product instances and their quantities.

        Returns:
            float: The total price of the order.
        """
        return sum(product.buy(quantity) for product, quantity in shopping_list)
