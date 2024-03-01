from homework_OOP.code.category_order_abc import CategoryOrderABC
from homework_OOP.code.product_error import ProductZeroError


class Order(CategoryOrderABC):
    """
    Класс, описывающий информацию о заказе
    """
    def __init__(self, name: str, quantity: int, price: float):
        """
        :param name: наименовая товара
        :param quantity: количество
        :param price: цена
        """
        self.name = name
        try:
            if quantity != 0:
                self.quantity = quantity
        except ProductZeroError as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")
        self.price = price

    def total_cost(self):
        """
        :return: Общую стоимость заказа
        """
        return self.quantity * self.price
