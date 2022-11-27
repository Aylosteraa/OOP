import math


class Rational:

    def __init__(self, a=1, b=1):
        self.__numerator = a
        self.__denominator = b

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, float | int):
            raise TypeError()
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, float | int):
            raise TypeError()
        if value == 0:
            raise ZeroDivisionError("Division by zero.")
        self.__denominator = value


    def __str__(self):
        return f'({self.__numerator}, {self.__denominator})'
    #def __str__(self):
    #   c = math.gcd(self.__numerator, self.__denominator)
    #   return f'{int(self.__numerator/c)}/{int(self.__denominator/c)}'

    def fraction(self):
        return float(self.__numerator/self.__denominator)

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented()
        new_denominator = math.lcm(self.__denominator, other.__denominator)
        self.__numerator = self.__numerator * int(new_denominator/self.__denominator)
        other.__numerator = other.__numerator * int(new_denominator / other.__denominator)
        new_numerator = self.__numerator + other.__numerator
        c = math.gcd(new_numerator, new_denominator)
        return Rational(int(new_numerator / c), int(new_denominator / c))

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented()
        new_denominator = math.lcm(self.__denominator, other.__denominator)
        self.__numerator = self.__numerator * int(new_denominator/self.__denominator)
        other.__numerator = other.__numerator * int(new_denominator / other.__denominator)
        new_numerator = self.__numerator - other.__numerator
        c = math.gcd(new_numerator, new_denominator)
        return Rational(int(new_numerator / c), int(new_denominator / c))

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented()
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        c = math.gcd(new_numerator, new_denominator)
        return Rational(int(new_numerator / c), int(new_denominator / c))

    def __truediv__(self, other):
        if not isinstance(other, Rational) or other.fraction == 0:
            return NotImplemented()
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        c = math.gcd(new_numerator, new_denominator)
        return Rational(int(new_numerator / c), int(new_denominator / c))

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented()
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __ne__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented()
        return self.__numerator != other.__numerator and self.__denominator != other.__denominator


frac1 = Rational(4, 16)
frac2 = Rational()
frac = frac1 + frac2
print(frac1 != frac2)
print(frac)
