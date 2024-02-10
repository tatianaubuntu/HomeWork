import json

from homework_13.code.Category import Category
from homework_13.code.Product import Product
from homework_13.config import FILE_JSON


def main():
    """
    :return: Списки с информацией о категориях и товарах
    """
    with open(FILE_JSON) as file:
        raw_json = file.read()
        products = json.loads(raw_json)
    for i in range(len(products)):
        products_ = []
        for prod in range(len(products[i]["products"])):
            product = Product(products[i]["products"][prod]["name"], products[i]["products"][prod]["description"],
                              products[i]["products"][prod]["price"], products[i]["products"][prod]["quantity"])
            products_.append({"name": product.title,
                              "description": product.description,
                              "price": product.price,
                              "quantity": product.quantity_in_stock})
        category = Category(products[i]['name'], products[i]['description'], products_)
        return category.products


if __name__ == '__main__':
    print(main())
