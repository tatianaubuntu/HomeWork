import pytest

from homework_OOP.code.product import Product


@pytest.fixture
def product_fixture():
    return (Product('Молоко', 'ценный пищевой продукт', 100.05, 5),
            Product('Молоко', 'ценный пищевой продукт', 150, 4),
            Product('Молоко', 'ценный пищевой продукт', 100, 4))


def test_product(product_fixture):
    assert product_fixture[0].name == 'Молоко'
    assert product_fixture[0].description == 'ценный пищевой продукт'
    assert product_fixture[0].price == 100.05
    assert product_fixture[0].quantity == 5
    product_fixture[0].price = 150
    assert product_fixture[0].price == 150
    product_fixture[0].price = 0
    assert product_fixture[0].price == 150
    product_fixture[0].price = 100
    assert product_fixture[0].price == 100
    product_fixture[0].cor_product({
        "name": 'Молоко',
        "description": 'ценный пищевой продукт',
        "price": 150,
        "quantity": 5
      })
    assert product_fixture[0].quantity == 10
    assert product_fixture[0].price == 150
    assert str(product_fixture[0]) == 'Молоко, 150 руб. Остаток: 10 шт.'
    assert product_fixture[0].__add__(product_fixture[1]) == 2100
