from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.products_abc import ProductsABC


class Product(ProductsABC, ObjectMixin):
    """ Класс, описывающий информацию о товарах"""

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена")
        elif 0 < new_price < self.__price:
            enter = input("Снизить стоимость товара? (y/n): ").lower()
            if enter == "y":
                self.__price = new_price
        elif new_price > self.__price:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        """
        :param product_data: новый продукт
        :return: добавление нового продукта
        """
        return cls(**product_data)

    def cor_product(self, product_data):
        """
        :param product_data: новый продукт
        Метод складывает количество товара, если он повторяется и корректирует стоимость на более высокую
        """
        new_product = self.__class__.new_product(product_data)
        if new_product.name == self.name:
            self.quantity += new_product.quantity
            if self.price <= new_product.price:
                self.price = new_product.price

    def __str__(self):
        """
        :return: Имя товара, стоимость и его наличие
        """
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, product):
        """
        :param product: экземпляр класса
        :return: общую стоимость продукта, если экземпляры одного класса
        """
        if type(product) != type(self):
            raise TypeError('Разные классы')
        return (self.__price * self.quantity) + (product.__price * product.quantity)
