from homework_OOP.code.category_order_abc import CategoryOrderABC


class Order(CategoryOrderABC):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_cost(self):
        return self.quantity * self.price
