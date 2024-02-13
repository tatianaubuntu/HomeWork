import pytest

from homework_OOP.code.category import Category


@pytest.fixture
def category_fixture():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [
                        {
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5
                        },
                        {
                            "name": "Iphone 15",
                            "description": "512GB, Gray space",
                            "price": 210000.0,
                            "quantity": 8
                        }
                    ])


def test_init_category(category_fixture):
    assert category_fixture.name == "Смартфоны"
    assert category_fixture.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category_fixture.total_number_of_unique_products == 2
    category_fixture.add_product({
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    })
    assert category_fixture.products == ['Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.',
                                         'Iphone 15, 210000 руб. Остаток: 8 шт.',
                                         'Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.']
    assert category_fixture.total_number_of_categories == 1
    assert category_fixture.total_number_of_unique_products == 3
    assert category_fixture.__str__() == 'Смартфоны, количество продуктов: 3 шт.'
