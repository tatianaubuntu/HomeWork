from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.product import Product


class Smartphone(Product, ObjectMixin):
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
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)
