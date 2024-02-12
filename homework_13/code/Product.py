class Product:
    """ Класс, описывающий информацию о товарах"""
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def new_product(cls, product_data):
        title = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity_in_stock = product_data['quantity']
        return cls(title, description, price, quantity_in_stock)

    def cor_product(self, product_data):
        new_product = Product.new_product(product_data)
        if new_product.title == self.title:
            self.quantity_in_stock += new_product.quantity_in_stock
            if self.price <= new_product.price:
                self.price = new_product.price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена")
        elif 0 < new_price < self.__price:
            enter = input("Снизить стоимость товара? (y/n): ").lower()
            if enter == "y":
                self.__price = new_price
        elif new_price > self.__price:
            self.__price = new_price
