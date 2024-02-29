from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.product import Product


class LawnGrass(Product, ObjectMixin):
    """ Класс, описывающий информацию о газонной траве"""

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str,
                 country: str,
                 germination_period: int):
        self.country = country
        self.germination_period = germination_period
        super().__init__(name, description, price, quantity, color)

