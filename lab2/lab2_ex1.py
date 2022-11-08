import random
import json
import datetime


class Ticket:
    title = 'Ticket'

    def __init__(self, price, discount):
        self.price = price
        self.unique_number = random.randint(100000, 999999)
        self.discount = discount

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
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Discount is int or float number")
        if not -1 <= value <= 1:
            raise ValueError("Discount is number larger than 0 and less than 1")
        self.__discount = value

    def construct_ticket(self):
        with open('sample.json', 'r') as openfile:
            json_object = json.load(openfile)
        for i in json_object['tickets']:
            if i['unique_number'] == self.unique_number:
                print(i)

    def ticket_price(self):
        self.price = self.price + self.price * self.discount
        return self.price

    def __str__(self):
        return f'{self.title}\n{self.unique_number}:\n{self.price}\nDiscount price: {self.ticket_price()}'


class RegularTicket(Ticket):
    title = 'Regular Ticket'

    def __init__(self, price, discount=0):
        super().__init__(price, discount)


class AdvanceTicket(Ticket):
    title = 'Advance Ticket'

    def __init__(self, price, discount=-0.4):
        super().__init__(price, discount)


class StudentTicket(Ticket):
    title = 'Student Ticket'

    def __init__(self, price, discount=-0.5):
        super().__init__(price, discount)


class LateTicket(Ticket):
    title = 'Late Ticket'

    def __init__(self, price, discount=0.1):
        super().__init__(price, discount)


class Event:

    def __init__(self, event, year, month, day, time, late=10, advance=60):
        self.event = event
        if not isinstance(year, int):
            raise TypeError()
        if year < 0:
            ValueError()
        if not isinstance(month, int):
            raise TypeError()
        if not 0 < month <= 12:
            ValueError()
        if not isinstance(day, int):
            raise TypeError()
        if not 0 < day <= 31:
            ValueError()
        self.date = datetime.date(year, month, day)
        self.time = time
        self.late = late
        self.advance = advance

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self.__event = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self.__time = value

    @property
    def late(self):
        return self.__late

    @late.setter
    def late(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__late = value

    @property
    def advance(self):
        return self.__advance

    @advance.setter
    def advance(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__advance = value

    def ticket(self, student=False):
        today = datetime.date.today()
        days = (self.date - today).days
        if student is True:
            return StudentTicket
        elif self.late < days < self.advance:
            return RegularTicket
        elif days >= self.advance:
            return AdvanceTicket
        elif days <= self.late:
            return LateTicket


def write_json(list_obj):
    if not isinstance(list_obj, list):
        raise TypeError
    list_dict = []
    for i in list_obj:
        list_dict.append(i.__dict__)
    dictionary = {'tickets': list_dict}
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)


event1 = Event('a', 2023, 1, 30, '6 p.m')
ticket1 = event1.ticket()(800)
event2 = Event('b', 2022, 11, 11, '6 p.m')
ticket2 = event2.ticket()(800)
ticket3 = event2.ticket(True)(800)
event3 = Event('c', 2022, 11, 30, '6 p.m')
ticket4 = event3.ticket()(800)
print(ticket4)
tickets = [ticket1, ticket2, ticket3, ticket4]
write_json(tickets)
ticket1.construct_ticket()




