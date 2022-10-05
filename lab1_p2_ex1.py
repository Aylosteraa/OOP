import sys


class Rectangle:
    length = 1.0
    width = 1.0

    def setter(self, x, y):
        if not (isinstance(x, float) and isinstance(y, float) and x > 0.0 and y > 0.0 and x < 20.0 and y < 20.0):
            sys.exit("Error! Length and width are numbers larger than 0.0 and less than 20.0")
        self.length = x
        self.width = y

    def getter(self):
        return self.length, self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


rect = Rectangle()
rect.setter(12.2, 8.1)
print(rect.getter())
print(rect.perimeter())
print(rect.area())
