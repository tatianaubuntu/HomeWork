from homework_OOP.code.category_order_abc import CategoryOrderABC
from homework_OOP.code.object_mixin import ObjectMixin
from homework_OOP.code.product import Product


class Category(ObjectMixin, CategoryOrderABC):
    """ Класс, описывающий категории товаров"""
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        super().__init__()
        self.name = name
        self.description = description
        self.__products = products

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError('Добавлять можно только объекты Product и дочерние от них.')
        Category.total_number_of_unique_products += 1
        self.__products.append(product)

    @property
    def products(self):
        product_info = []
        for prod in self.__products:
            product_info.append(f'{prod.name}, {int(prod.price)} руб. Остаток: {prod.quantity} шт.')
        return product_info

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def total_cost(self):
        product_cost_list = []
        for prod in self.__products:
            product_cost_list.append(prod.price * prod.quantity)
        return sum(product_cost_list)


