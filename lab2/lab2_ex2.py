import datetime
import json


class Pizza:
    __all_size = (30, 40)

    def __init__(self, price, ingredients, size=30):
        self.price = price
        self.ingredients = ingredients
        self.size = size
        self.extra = []

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list):
            raise TypeError()
        self.__ingredients = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int | float):
            raise TypeError()
        if value not in self.__all_size:
            raise ValueError()
        self.__size = value

    def add_extra(self, extra_ingredients, extra_price):
        if not isinstance(extra_ingredients, str):
            raise TypeError()
        if not isinstance(extra_price, int | float):
            raise TypeError()
        if extra_price < 0:
            raise ValueError()
        self.extra.append(extra_ingredients)
        self.price += extra_price

    def __str__(self):
        comp = '\n'
        for i in self.ingredients:
            comp += f'{i}\n'
        ingr = '\n'
        for i in self.extra:
            ingr += f'{i}\n'
        return f'Ingredients:{comp}Size: {self.size}cm\nExtra ingredients:{ingr}\n-------------\nPrice: {self.price}'


class HawaiianPizza(Pizza):
    title = 'Hawaiian Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


class NeapolitanPizza(Pizza):
    title = 'Neapolitan Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


class CaliforniaPizza(Pizza):
    title = 'California Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


class SicilianPizza(Pizza):
    title = 'Sicilian Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)


class GreekPizza(Pizza):
    title = ' Greek Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


class DetroitPizza(Pizza):
    title = 'Detroit Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


class ChicagoPizza(Pizza):
    title = 'Chicago Pizza'

    def __init__(self, price, ingredients, size):
        super().__init__(price, ingredients, size)

    def __str__(self):
        return f'{self.title}\n' + super().__str__()


def get_pizza():
    today = datetime.date.today()
    with open('pizza_of_the_day.json', 'r') as file:
        json_object = json.load(file)
        return eval(json_object[str(today.isoweekday())])


pizza1 = get_pizza()(450, ['a', 'h', 'n', 'ht'], 30)
pizza1.add_extra('d', 10)
print(pizza1)
