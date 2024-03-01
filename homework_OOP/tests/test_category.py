import pytest

from homework_OOP.code.product_error import ProductZeroError, ProductClassError


def test_init_category(category, product3, shop, product4, category1):
    """
    :param category: Фикстура класса "Category"
    :param product3: Фикстура класса "Product"
    :param shop: Фикстура класса "Shop"
    :param product4: Фикстура класса "Product"
    :return: Тестирование атрибутов и методов класса "Category"
    """
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.total_number_of_unique_products == 2

    category.add_product(product3)
    assert category.products == ['Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.',
                                 'Iphone 15, 210000 руб. Остаток: 8 шт.',
                                 'Iphone 10, 210000 руб. Остаток: 8 шт.']

    assert category.total_number_of_categories == 2
    assert category.total_number_of_unique_products == 3

    assert category.__str__() == 'Смартфоны, количество продуктов: 3 шт.'

    # with pytest.raises(ProductClassError):
    #     category.add_product(shop)

    assert category.total_cost() == 4260000.0

    # with pytest.raises(ProductZeroError):
    #     category.add_product(product4)

    assert category.average_price() == 200000.0
    assert category1.average_price() == 0
