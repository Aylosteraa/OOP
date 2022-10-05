import sys
import math


class Rational:

    def __init__(self, a=1, b=1):
        if not (isinstance(a, float) and isinstance(b, float)):
            sys.exit("Error!")
        if b == 0:
            sys.exit("Error! Division by zero.")
        c = math.gcd(a, b)
        self.__numerator = int(a/c)
        self.__denominator = int(b/c)

    def fraction(self):
        print(str(self.__numerator) + '/' + str(self.__denominator))

    def fp(self):
        print(float(self.__numerator/self.__denominator))


frac = Rational(20, 25)
frac.fraction()
frac.fp()
