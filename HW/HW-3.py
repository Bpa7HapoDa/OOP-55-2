class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def get_info(self):
        print(f'Товар:{self.__name}, Цена:{self.__price}, Кол-во:{self.__stock}')
    def buy(self, quantity):
        if self.__stock >= quantity:
            self.__stock -= quantity
            return True
        return False
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Cart():
    def __init__(self, products):
        self.products = []

    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.products.append((product, quantity))
            print(f"Добавлено в корзину: {product.get_name()}, {quantity} шт.")
        else:
            print(f"Недостаточно товара '{product.get_name()}' на складе. В наличии: {product._Product__stock} шт.")






p1 = Product('Notebook','50000', '2')
p1.buy()