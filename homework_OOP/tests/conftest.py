import pytest

from homework_OOP.code.category import Category
from homework_OOP.code.lawn_grass import LawnGrass
from homework_OOP.code.product import Product
from homework_OOP.code.shop import Shop
from homework_OOP.code.smartphone import Smartphone


@pytest.fixture
def category_fixture():
    return (Category("Смартфоны",
                     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                     [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                              180000.0, 5, 'white'), Product("Iphone 15", "512GB, Gray space",
                                                             210000.0, 8, 'white')]),
            Smartphone('OnePlus 10Pro 12/256Gb Volcan Bl',
                       'Смартфон OnePlus 10 Pro Volcanic Black работает на операционной системе Android 12, '
                       'за производительность отвечают восьмиядерный процессор Qualcomm и 8 Гб оперативной памяти',
                       150000,
                       15, 'black',
                       'Qualcomm Snapdragon 8 Gen 1 3 ГГц', '10 Pro', 256))


@pytest.fixture
def lawn_grass_fixture():
    return LawnGrass('lawn grass', 'трава газонная', 1000.00, 50, 'green',
                     'Russia', 1)


@pytest.fixture
def smartphone_fixture():
    return Smartphone('OnePlus 10Pro 12/256Gb Volcan Bl',
                      'Смартфон OnePlus 10 Pro Volcanic Black работает на операционной системе Android 12, '
                      'за производительность отвечают восьмиядерный процессор Qualcomm и 8 Гб оперативной памяти',
                      150000,
                      15, 'black',
                      'Qualcomm Snapdragon 8 Gen 1 3 ГГц', '10 Pro', 256)


@pytest.fixture
def product_fixture():
    return (Product('Молоко', 'ценный пищевой продукт', 100.05, 5, 'white'),
            Product('Молоко', 'ценный пищевой продукт', 150, 4, 'white'),
            Product('Молоко', 'ценный пищевой продукт', 100, 4, 'white'),
            Smartphone('OnePlus 10Pro 12/256Gb Volcan Bl',
                       'Смартфон OnePlus 10 Pro Volcanic Black работает на операционной системе Android 12, '
                       'за производительность отвечают восьмиядерный процессор Qualcomm и 8 Гб оперативной памяти',
                       150000,
                       15, 'black',
                       'Qualcomm Snapdragon 8 Gen 1 3 ГГц', '10 Pro', 256))


@pytest.fixture
def shop_fixture():
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                        [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                                 180000.0, 5, 'white'), Product("Iphone 15", "512GB, Gray space",
                                                                210000.0, 8, 'white')])
    return Shop(category)
