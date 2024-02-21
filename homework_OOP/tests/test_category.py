import pytest


def test_init_category(category, smartphone, shop):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.total_number_of_unique_products == 2
    category.add_product(smartphone)
    assert category.products == ['Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.',
                                 'Iphone 15, 210000 руб. Остаток: 8 шт.',
                                 'OnePlus 10Pro 12/256Gb Volcan Bl, 150000 руб. Остаток: 15 шт.']
    assert category.total_number_of_categories == 1
    assert category.total_number_of_unique_products == 3
    assert category.__str__() == 'Смартфоны, количество продуктов: 3 шт.'

    with pytest.raises(TypeError):
        category.add_product(shop)
