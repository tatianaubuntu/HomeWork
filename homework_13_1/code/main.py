import json

from homework_13_1.config import FILE_JSON


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
        self.products = products

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.products)


class Product:
    """ Класс, описывающий информацию о товарах"""
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


def main():
    """
    :return: Списки с информацией о категориях и товарах
    """
    with open(FILE_JSON) as file:
        raw_json = file.read()
        products = json.loads(raw_json)
        category_ = []
        product_ = []
    for i in range(len(products)):
        category = Category(products[i]["name"], products[i]["description"], products[i]["products"])
        category_.append(category.title)
        for prod in range(len(products[i]["products"])):
            product = Product(products[i]["products"][prod]["name"], products[i]["products"][prod]["description"],
                              products[i]["products"][prod]["price"], products[i]["products"][prod]['quantity'])
            product_.append(product.quantity_in_stock)

    return category_, product_


if __name__ == '__main__':
    print(main())
