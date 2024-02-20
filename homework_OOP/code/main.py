import json

from homework_OOP.code.category import Category
from homework_OOP.code.product import Product
from homework_OOP.config import FILE_JSON


def main():
    """
    :return: Списки с информацией о категориях и товарах
    """
    with open(FILE_JSON) as file:
        raw_json = file.read()
        data = json.loads(raw_json)
        categories = []
        for cat_data in data:
            products_instances = []
            for product_data in cat_data['products']:
                new_product = Product.new_product(product_data)
                products_instances.append(new_product)
            category = Category(cat_data['name'], cat_data['description'], products_instances)
            categories.append(category)
        print(categories)


if __name__ == '__main__':
    main()
