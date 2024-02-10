class Category:
    """ Класс, описывающий категории товаров"""
    title: str
    description: str
    products: list
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.__products)

    @property
    def products(self):
        product_info = []
        for prod in self.__products:
            product_info.append(f'{prod["name"]}, {int(prod["price"])} руб. Остаток: {prod["quantity"]} шт.')
        return '\n'.join(product_info)

