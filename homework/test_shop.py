"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():  # экземпляр класса продукта
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_basket():  # экземпляр класса корзины
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    # Проверка метода check_quantity
    def test_product_check_quantity_int_1000(self, product):  # положительная проверка на передачу параметра quantity в функцию check_quantity с типом данных - integer.
                                                            # Здесь также учитывается положительная проверка граничного значения параметра quantity: 1000.
                                                            # В таких проверках хорошо было бы применить параметризацию, но в рамках этого дз это не требуется.
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) == True

    def test_product_check_quantity_int_1001(self, product):  # положительная проверка передачи граничного значения параметра quantity в функцию check_quantity: 1001
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1001) == False

    def test_product_check_quantity_int_1010(self, product):  # положительная проверка передачи граничного значения параметра quantity в функцию check_quantity: 1010
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1010) == False

    def test_product_check_quantity_int_999(self, product):  # положительная проверка передачи граничного значения параметра quantity в функцию check_quantity: 999
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) == True

    def test_product_check_quantity_int_900(self, product):  # положительная проверка передачи граничного значения параметра quantity в функцию check_quantity: 900
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(900) == True

    def test_product_check_quantity_str(self, product):  # негативная проверка на передачу параметра quantity с типом данных - str
        with pytest.raises(TypeError) as exc_info:
            Product.check_quantity(Product(name=product.name, price=product.price, description=product.description,
                                           quantity=str(product.quantity)), 1000)
        assert "'<=' not supported between instances of 'int' and 'str'" in str(exc_info.value)

    #  Здесь должна была быть проверка на предачу в параметр quantity тип данных - bool. Но так как булевы значения являются подклассом типа данных int, при выполнении
    #  операции сравнения в методе check_quantity, возвращается логический тип данных - True. Это не совсем корректнная проверка в данном контексте подмены числового типа
    #  данных на булево значение.

    # Проверка метода buy
    def test_correct_buy_product(self, product):  # положительная проверка метода buy. Передаем quantity = 1000
        # TODO напишите проверки на метод buy
        assert product.buy(1000) == True

    def test_incorrect_buy_product(self, product):  # негативная проверка метода buy. Передаем в параметр quantity тип данных - str
        # TODO напишите проверки на метод buy
        with pytest.raises(TypeError) as exc_info:
            Product.buy(Product(name=product.name, price=product.price, description=product.description,
                                quantity=str(product.quantity)), 1000)
        assert "'<=' not supported between instances of 'int' and 'str'" in str(exc_info.value)

    def test_product_buy_more_than_available(self, product):  # Положительная проверка. Ожидаем ValueError, если хотим купить больше, чем есть в магазине
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert product.buy(1001) == ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    #  Проверки добавления продукта в корзину
    def test_add_product_in_basket(self, product,
                                   product_basket):  # положительная проверка добавления продукта в корзину
        assert product in product_basket.add_product(product, 2)

    def test_add_2_same_product_in_basket(self, product,
                                          product_basket):  # положительная проверка того, что если в корзине уже есть продукт, то
        # при добавлении того же продукта количество этого продукта будет = 2
        product_basket.add_product(product, 2)
        assert product_basket.products[product] == 2

    def test_incorrect_type_buy_count(self, product,
                                      product_basket):  # негативная проверка: возврат текста ошибки при передаче
        # в параметр buy_count тип данных - str
        add_inc_type_buy_count = product_basket.add_product(product, '2')
        assert add_inc_type_buy_count == 'Тип данных в параметре buy_count должен быть = int'

    # проверка удаления товаров из корзины
    def test_remove_all_products_in_cart(self, product,
                                         product_basket):  # положительная проверка на полное удаление товаров из корзины
        product_basket.add_product(product, 2)  # вызов метода добавления товаров в корзину
        product_basket.remove_product(product)  # вызов метода удаления товаров из корзины
        assert product_basket.products == {}

    def test_remove_some_products_in_cart(self, product,
                                     product_basket):  # положительная проверка изменения количества товаров в корзине
        product_basket.add_product(product, 6)  # в корзину добавляется 6 товаров
        product_basket.remove_product(product, 2)  # удаляем 2 товара у одного и того же экземпляра класса
        assert product_basket.products[product] == 4

    def test_remove_cart_with_incorrect_type_remove_count(self, product, product_basket):  # негативная проверка удаления товара из
        # корзины с передачей в параметр remove_count тип данных - str
        product_basket.add_product(product, 6)
        with pytest.raises(TypeError) as exc_info:
            product_basket.remove_product(product, '2')
        assert "'>' not supported between instances of 'str' and 'int'" in str(exc_info.value)

    def test_clear_cart(self, product, product_basket): # положительная проверка полного удаления товаров в корзине
        product_basket.add_product(product, 6)
        product_basket.clear()
        assert product_basket.products == {}

    def test_get_full_price_1_product(self, product, product_basket): # положительная проверка получения полной цены 1 товара в корзине
        product_basket.add_product(product, 6)
        assert product_basket.get_total_price() == 600

    def test_get_full_price_several_product(self, product, product_basket): # положительная проверка получения полной цены нескольких товара в корзине
        product_basket.add_product(product, 6)
        product_basket.add_product(Product("book", 800, "This is a book", 1000), 6)  # добавили еще 1 товар стоимостью 5400,
                                                                                                                            # в количестве 6 экземпляров
        assert product_basket.get_total_price() == 5400

    def test_buy_all_product_in_stock(self, product, product_basket): # положительная проверка покупки всех товаров в корзине
        product_basket.add_product(Product("book", 800, "This is a book", 1000), 6)
        product_basket.buy()
        assert product_basket.products == {}

    def test_buy_product_less_than_in_stock(self, product, product_basket): # положительная проверка покупки всех товаров в корзине: если количество товаров в корзине < 1000 (не хватает количества товаров на складе)
        product_basket.add_product(Product("book", 800, "This is a book", 999), 6)
        assert product_basket.buy() == ValueError
