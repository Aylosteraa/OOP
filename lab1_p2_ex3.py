class Product:

    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:

    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone


class Order:

    def calculate(self, pr_list):
        sum = 0
        for i in pr_list:
            sum += i.price
        print("SUM = ", sum, sep=" ")

    def information(self, cust, pr_list):
        print("Customer:", cust.surname, cust.name, cust.patronymic, cust.mobile_phone, sep=" ")
        print("Products:")
        for i in pr_list:
            print(i.price, i.description, i.dimensions, sep="   ")


cust = Customer('Barabash', 'Marina', 'Volodymyrivna', '099-526-73-10')
prod = []
orde = Order()

prod.append(Product(125, "product 1", "10x45x62"))
prod.append(Product(100, "product 2", "10x14x50"))
prod.append(Product(800, "product 3", "14x72x12"))
prod.append(Product(145, "product 4", "30x20x30"))

orde.information(cust, prod)
orde.calculate(prod)



