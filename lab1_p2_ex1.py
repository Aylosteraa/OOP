class Rectangle:


    def __init__(self, x=1, y=1):
        if not isinstance(x, float | int):
            raise TypeError("Length is float-point number")
        if not isinstance(y, float | int):
            raise TypeError("Width is float-point number")
        if not 0 < x < 20:
            raise ValueError("Length is number larger than 0.0 and less than 20.0")
        if not 0 < y < 20:
            raise ValueError("Width is numbers larger than 0.0 and less than 20.0")
        self.length = x
        self.width = y

    def setter(self, x, y):
        if not isinstance(x, float | int):
            raise TypeError("Length is float-point number")
        if not isinstance(y, float | int):
            raise TypeError("Width is float-point number")
        if not 0 < x < 20:
            raise ValueError("Length is number larger than 0.0 and less than 20.0")
        if not 0 < y < 20:
            raise ValueError("Width is numbers larger than 0.0 and less than 20.0")
        self.length = x
        self.width = y

    def getter(self):
        return self.length, self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


rect = Rectangle(12, 14.1)
print(rect.getter())
print(rect.perimeter())
print(rect.area())
rect.setter(10, 2.3)
print(rect.getter())
print(rect.perimeter())
print(rect.area())
