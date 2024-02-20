import pytest


def test_init_category(category_fixture):
    assert category_fixture[0].name == "Смартфоны"
    assert category_fixture[0].description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category_fixture[0].total_number_of_unique_products == 2
    category_fixture[0].add_product(category_fixture[1])
    assert category_fixture[0].products == ['Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.',
                                            'Iphone 15, 210000 руб. Остаток: 8 шт.',
                                            'OnePlus 10Pro 12/256Gb Volcan Bl, 150000 руб. Остаток: 15 шт.']
    assert category_fixture[0].total_number_of_categories == 1
    assert category_fixture[0].total_number_of_unique_products == 3
    assert category_fixture[0].__str__() == 'Смартфоны, количество продуктов: 3 шт.'

    with pytest.raises(ValueError):
        category_fixture[0].add_product(category_fixture[0])
