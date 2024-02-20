from homework_OOP.code.product import Product


class LawnGrass(Product):
    """ Класс, описывающий информацию о газонной траве"""
    def __init__(self, country, germination_period, color, name, description, price, quantity):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

