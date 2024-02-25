from abc import ABC, abstractmethod


class ProductsABC(ABC):
    """Абстрактный класс продуктов"""

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @abstractmethod
    def keeping(self):
        """
        Метод, который показывает информацию о хранении
        """
        pass
