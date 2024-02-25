def test_object_mixin(lawn_grass, product1, smartphone):
    assert lawn_grass.__repr__() == ("LawnGrass({'name': 'lawn grass', 'description': 'трава газонная', "
                                     "'_ProductsABC__price': 1000.0, 'quantity': 50, 'color': 'green', 'country': "
                                     "'Russia', 'germination_period': 1})")
    assert product1.__repr__() == ("Product({'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый "
                                   "цвет, 200MP камера', '_ProductsABC__price': 180000.0, 'quantity': 5, "
                                   "'color': 'white', '_Product__price': 180000.0})")
    assert smartphone.__repr__() == ("Smartphone({'name': 'OnePlus 10Pro 12/256Gb Volcan Bl', 'description': "
                                     "'Смартфон OnePlus 10 Pro Volcanic Black работает на операционной системе "
                                     'Android 12, за производительность отвечают восьмиядерный процессор Qualcomm '
                                     "и 8 Гб оперативной памяти', '_ProductsABC__price': 150000, 'quantity': 15, "
                                     "'color': 'black', 'efficiency': 'Qualcomm Snapdragon 8 Gen 1 3 ГГц', "
                                     "'model': '10 Pro', 'memory': 256})")
