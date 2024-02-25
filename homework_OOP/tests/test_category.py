import pytest


def test_init_category(category, product3, shop):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.total_number_of_unique_products == 2
    category.add_product(product3)
    assert category.products == ['Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.',
                                 'Iphone 15, 210000 руб. Остаток: 8 шт.',
                                 'Iphone 10, 210000 руб. Остаток: 8 шт.']
    assert category.total_number_of_categories == 1
    assert category.total_number_of_unique_products == 3
    assert category.__str__() == 'Смартфоны, количество продуктов: 3 шт.'

    with pytest.raises(TypeError):
        category.add_product(shop)

    assert category.total_cost() == 4260000.0
