from abc import ABC, abstractmethod


class ProductsABC(ABC):
    """Абстрактный класс продуктов"""

    def __init__(self):
        super().__init__()

    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        """
        Метод, который добавляет новый продукт
        """
        pass



