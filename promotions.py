"""
Promotions.py
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract class that represents a promotion.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscountPromotion(Promotion):
    """
    Class that represents a percentage discount promotion.
    """

    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percentage / 100)


class SecondHalfPricePromotion(Promotion):
    """
    Class that represents a second item at half price promotion.
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity // 2 + quantity % 2
        half_price_quantity = quantity // 2
        return product.price * (full_price_quantity + half_price_quantity / 2)


class BuyTwoGetOneFreePromotion(Promotion):
    """
    Class that represents a buy two get one free promotion.
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        return product.price * (quantity - quantity // 3)
