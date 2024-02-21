from homework_OOP.code.product import Product


class Smartphone(Product):
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
