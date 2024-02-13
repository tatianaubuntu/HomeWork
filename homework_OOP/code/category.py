class Category:
    """ Класс, описывающий категории товаров"""
    name: str
    description: str
    products: list
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_number_of_unique_products += 1

    @property
    def products(self):
        product_info = []
        for prod in self.__products:
            product_info.append(f'{prod["name"]}, {int(prod["price"])} руб. Остаток: {prod["quantity"]} шт.')
        return product_info

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'



