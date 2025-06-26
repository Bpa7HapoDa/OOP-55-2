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
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.products.append((product, quantity))
            print(f"Добавлено в корзину: {product.get_name()}, {quantity} шт.")
        else:
            print(f"Недостаточно товара '{product.get_name()}' на складе. В наличии: {product._Product__stock} шт.")

    def checkout(self):
        total_sum = 0
        print("\n--- Ваш заказ ---")
        for product, quantity in self.products:
            item_total = product.get_price() * quantity
            print(f"Товар: {product.get_name()}, {quantity} шт. по {product.get_price()} = {item_total}")
            total_sum += item_total
        print(f"Итого: {total_sum}")

p1 = Product("Ноутбук", 50000, 10)
p2 = Product("Мышка", 1000, 50)
p3 = Product("Клавиатура", 3000, 5)

cart = Cart()

cart.add_product(p1, 2)
cart.add_product(p2, 5)
cart.add_product(p3, 3) # Добавляем клавиатуру
cart.add_product(p1, 10) # Попытка купить больше ноутбуков, чем есть на складе

print("\n--- Состояние склада после добавления в корзину ---")
print(p1.get_info())
print(p2.get_info())
print(p3.get_info())


cart.checkout()




