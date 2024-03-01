import contextlib
import io


def test_object_mixin(lawn_grass, product1, smartphone, category):
    assert repr(lawn_grass) == ("LawnGrass({'name': 'lawn grass', 'description': 'трава газонная', "
                                "'_Product__price': 1000.0, 'quantity': 50, 'color': 'green', 'country': "
                                "'Russia', 'germination_period': 1})")
    assert repr(product1) == ("Product({'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый "
                              "цвет, 200MP камера', '_Product__price': 180000.0, 'quantity': 5, 'color': "
                              "'white'})")
    assert repr(smartphone) == ("Smartphone({'name': 'OnePlus 10Pro 12/256Gb Volcan Bl', 'description': "
                                "'Смартфон OnePlus 10 Pro Volcanic Black работает на операционной системе "
                                'Android 12, за производительность отвечают восьмиядерный процессор Qualcomm '
                                "и 8 Гб оперативной памяти', '_Product__price': 150000, 'quantity': 15, "
                                "'color': 'black', 'efficiency': 'Qualcomm Snapdragon 8 Gen 1 3 ГГц', "
                                "'model': '10 Pro', 'memory': 256})")
    assert repr(category) == ("Category({'name': 'Смартфоны', 'description': 'Смартфоны, как средство не "
                              'только коммуникации, но и получение дополнительных функций для удобства '
                              "жизни', '_Category__products': [Product({'name': 'Samsung Galaxy C23 Ultra', "
                              "'description': '256GB, Серый цвет, 200MP камера', '_Product__price': "
                              "180000.0, 'quantity': 5, 'color': 'white'}), Product({'name': 'Iphone 15', "
                              "'description': '512GB, Gray space', '_Product__price': 210000.0, 'quantity': "
                              "8, 'color': 'white'})]})")
