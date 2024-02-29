class ObjectMixin:
    """
    Класс, который информирует о создании объекта с атрибутами
    """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
