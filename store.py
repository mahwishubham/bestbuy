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
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        if isinstance(products, list) and all(isinstance(product, Product) for product in products):
            self._products = products
        else:
            raise TypeError("Products should be a list of Product instances")

    def __str__(self):
        p = ""
        for i in range(len(self._products)):
            product = self._products[i]
            p += f'{product._id}: {str(product)} \n'
        return p

    def __lt__(self, other: 'Store') -> bool:
        return self.get_total_value() < other.get_total_value()

    def __gt__(self, other: 'Store') -> bool:
        return self.get_total_value() > other.get_total_value()

    def __contains__(self, item) -> bool:
        for product in self.products:
            if product.name == item or product.id == item:
                return True
        return False

    def __add__(self, other: 'Store') -> 'Store':
        return Store(self._products + other.products)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)

    def get_total_value(self) -> float:
        return sum(product.price * product.quantity for product in self.products)

    def find_product(self, product_name) -> Union[Product, None]:
        for product in self.products:
            if product_name in [product.name, product.id]:
                return product
        return None

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        return sum(product.buy(quantity) for product, quantity in shopping_list)
