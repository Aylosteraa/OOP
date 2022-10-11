import math


class Rational:

    def __init__(self, a=1, b=1):
        if not isinstance(a, float | int):
            raise TypeError()
        if not isinstance(b, float | int):
            raise TypeError()
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        self.__numerator = a
        self.__denominator = b

    def __str__(self):
        c = math.gcd(self.__numerator, self.__denominator)
        return f'{int(self.__numerator/c)}/{int(self.__denominator/c)}'

    def fraction(self):
        return f'{float(self.__numerator/self.__denominator)}'


frac = Rational(4, 16)
print(frac)
print(frac.fraction())
