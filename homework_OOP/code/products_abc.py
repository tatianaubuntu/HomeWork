from abc import ABC, abstractmethod


class ProductsABC(ABC):
    """Абстрактный класс продуктов"""
    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        """
        Метод, который добавляет новый продукт
        """
        pass



