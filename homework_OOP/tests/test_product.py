import pytest


def test_product(product1, product2, lawn_grass):
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    product1.price = 190000.0
    assert product1.price == 190000.0
    product1.price = 0
    assert product1.price == 190000.0
    product1.price = 180000.0
    assert product1.price == 180000.0
    product1.cor_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "color": "white"
      })
    assert product1.quantity == 10
    assert product1.price == 180000.0
    assert str(product1) == 'Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 10 шт.'
    assert product1.__add__(product2) == 3480000.0
    with pytest.raises(TypeError):
        product1.__add__(lawn_grass)
