import pytest

from homework_13.code.Product import Product


@pytest.fixture
def product_fixture():
    return (Product('Молоко', 'ценный пищевой продукт',
                    100.05, 5))


def test_product(product_fixture):
    assert product_fixture.title == 'Молоко'
    assert product_fixture.description == 'ценный пищевой продукт'
    assert product_fixture.price == 100.05
    assert product_fixture.quantity_in_stock == 5
    product_fixture.price = 150
    assert product_fixture.price == 150
    product_fixture.price = 0
    assert product_fixture.price == 150
    product_fixture.price = 100
    assert product_fixture.price == 100
    product_fixture.cor_product()
    assert product_fixture.quantity_in_stock == 10
    assert product_fixture.price == 150
