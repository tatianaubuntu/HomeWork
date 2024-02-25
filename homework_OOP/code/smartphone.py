from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.products_abc import ProductsABC


class Smartphone(ProductsABC, ObjectMixin):
    """ Класс, описывающий информацию о смартфонах"""

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str,
                 efficiency: str,
                 model: str,
                 memory: int):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def keeping(self):
        """
        Метод, который показывает информацию о хранении смартфонов
        """
        print(f'Смартфон хранится в сухом месте при комнатной температуре')
