class ProductError(Exception):
    """
    Общий класс исключения
    """
    def __init__(self, *args):
        self.message = args if args else 'Неизвестная ошибка'

    def __str__(self):
        return self.message


class ProductClassError(ProductError):
    """
    Класс исключения объектов не относящихся к классу "Product" и его дочерних
    """
    def __init__(self, *args):
        self.message = args if isinstance(args, self.__class__) else 'Добавлять можно только объекты Product и дочерние от них'


class ProductZeroError(ProductError):
    """
    Класс исключения при нулевом количестве товара
    """
    def __init__(self, *args):
        self.message = args if args != 0 else 'Добавлять можно только объекты Product и дочерние от них'


