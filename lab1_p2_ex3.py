class Product:

    def __init__(self, price, description, dimensions):
        if not isinstance(price, float | int):
            raise TypeError()
        if price < 0:
            raise ValueError()
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.price}   {self.description}   {self.dimensions}'


class Customer:

    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.mobile_phone}'


class Order:

    def __init__(self, customer, prod_list):
        self.customer = customer
        self.prod_list = prod_list

    def calculate(self):
        sum = 0
        for i in self.prod_list:
            sum += i.price
        return sum

    def add_product(self, product):
        self.prod_list.append(product)

    def del_product(self, product):
        self.prod_list.remove(product)


    def count(self):
        dict = {}
        for i in self.prod_list:
            dict[i] = self.prod_list.count(i)
        return dict

    def __str__(self):
        string = '\n'
        dict = self.count()
        for key in dict:
            string += key.__str__() + f'  x  {dict[key]} \n'
        return f'{self.customer}{string}Total = {self.calculate()}'


cust = Customer('Barabash', 'Marina', 'Volodymyrivna', '099-526-73-10')
prod1 = (Product(125, "product 1", "10x45x62"))
prod2 = (Product(100, "product 2", "10x14x50"))
prod3 = (Product(800, "product 3", "14x72x12"))
prod4 = (Product(145, "product 4", "30x20x30"))
prod = [prod1, prod2, prod3, prod4]

pr_list = Order(cust, prod)

pr_list.add_product(prod1)
pr_list.add_product(prod2)
pr_list.add_product(prod1)
pr_list.del_product(prod3)
print(pr_list)
