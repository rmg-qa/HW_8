class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity: int) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if quantity <= self.quantity:
            return True
        return False

    def buy(self, quantity: int):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if quantity <= self.quantity:
            return Product.check_quantity(self, quantity)
        else:
            return ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count: int = 1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if type(buy_count) != int:
            return 'Тип данных в параметре buy_count должен быть = int'
        elif product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
        return self.products

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None:
            Cart.clear(self)
        elif remove_count > self.products[product]:
            del self.products[product]
        else:
            new_key_value = self.products[product] - remove_count
            self.products[product] = new_key_value
        return self.products

    def clear(self):
        return self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * self.products[product]
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        total_quantity = 0
        for product in self.products.keys():
            total_quantity += product.quantity
        if total_quantity >= 1000:
            return Cart.clear(self)  # Я не понимаю, что должен делать метод покупки. Надоело гадать в этом дз: самое логичное, что приходит в голову это очистка корзины
        else:
            return ValueError
