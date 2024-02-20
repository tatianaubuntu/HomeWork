def test_shop(shop_fixture):
    for product in shop_fixture:
        assert product == 'Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.' or 'Iphone 15, 210000 руб. Остаток: 8 шт.'



