import pytest

from homework_13_1.code.main import Category, Product


@pytest.fixture
def category_fixture():
    return Category('Молочные продукты', 'Пищевые продукты, вырабатываемые из молока',
                    ['сыр', 'молоко', 'кефир'], ['Молочные продукты'])


def test_init_category(category_fixture):
    assert category_fixture.title == 'Молочные продукты'
    assert category_fixture.description == 'Пищевые продукты, вырабатываемые из молока'
    assert category_fixture.products == ['сыр', 'молоко', 'кефир']
    assert category_fixture.total_number_of_categories == 1
    assert category_fixture.total_number_of_unique_products == 3


@pytest.fixture
def product_fixture():
    return Product('Молоко', 'ценный пищевой продукт, содержащий более 100 питательных веществ',
                   100.05, 5)


def test_product(product_fixture):
    assert product_fixture.title == 'Молоко'
    assert product_fixture.description == 'ценный пищевой продукт, содержащий более 100 питательных веществ'
    assert product_fixture.price == 100.05
    assert product_fixture.quantity_in_stock == 5
