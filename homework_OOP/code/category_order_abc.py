from abc import ABC, abstractmethod


class CategoryOrderABC(ABC):
    """
    Абстрактный класс категории и заказа
    """
    @abstractmethod
    def total_cost(self):
        """
        Абстрактный метод получения общей стоимости
        """
        pass
