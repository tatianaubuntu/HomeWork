from homework_OOP.code.product import Product


class LawnGrass(Product):
    """ Класс, описывающий информацию о газонной траве"""
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, country: str, germination_period: int):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
