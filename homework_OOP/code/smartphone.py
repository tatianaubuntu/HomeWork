from homework_OOP.code.product import Product


class Smartphone(Product):
    """ Класс, описывающий информацию о смартфонах"""

    def __init__(self, efficiency, model, memory, color, name, description, price, quantity):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

