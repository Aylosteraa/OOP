import datetime
from dateutil.relativedelta import relativedelta


class Calendar:

    def __init__(self, day, month, year):
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

    def __str__(self):
        return f'{self.date}'

    def __iadd__(self, other):
        if not isinstance(other, DaysMonthsYears):
            return NotImplemented()
        self.date += relativedelta(years=other.years, months=other.months, days=other.days)
        return self

    def __isub__(self, other):
        if not isinstance(other, DaysMonthsYears):
            return NotImplemented()
        self.date -= relativedelta(years=other.years, months=other.months, days=other.days)
        return self

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date == other.date

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date != other.date

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date < other.date

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date > other.date

    def __le__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date <= other.date

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            return NotImplemented()
        return self.date >= other.date


class DaysMonthsYears:

    def __init__(self, days=0, months=0, years=0):
        self.days = days
        self.months = months
        self.years = years

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__days = value

    @property
    def months(self):
        return self.__months

    @months.setter
    def months(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__months = value

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__years = value


day = Calendar(10, 10, 2004)
day1 = Calendar(15, 10, 2004)
print(day <= day1)
day -= DaysMonthsYears(months=15)
print(day)

