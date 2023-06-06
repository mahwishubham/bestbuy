from typing import List
from products import Product


class Store:
    """
    Store class represents a store with a list of products.
    """
    def __init__(self, products: List[Product]):
        """
        Initializes a Store instance with a list of products.

        Args:
            products (List[Product]): The list of products in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of items in the store.

        Returns:
            int: The total quantity of items in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products in the store.

        Returns:
            List[Product]: A list of all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def find_product(self, product_name: str):
        """
        Finds and returns a product in the store based on its name.

        Args:
            product_name (str): The name of the product to find.

        Returns:
            Product or None: The found Product instance or None if not found.
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Buys the products in the shopping list and returns the total price of the order.

        Args:
            shopping_list (List[tuple]): A list of tuples where each tuple contains a Product instance and its quantity.

        Returns:
            float: The total price of the order.
        """
        return sum(product.buy(quantity) for product, quantity in shopping_list)