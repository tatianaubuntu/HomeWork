from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.products_abc import ProductsABC


class LawnGrass(ProductsABC, ObjectMixin):
    """ Класс, описывающий информацию о газонной траве"""
    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 color: str,
                 country: str,
                 germination_period: int):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def keeping(self):
        """
        Метод, который показывает информацию о хранении газонной травы
        """
        print('Газонная трава хранится в помещении при температуре не выше +10 градусов')
