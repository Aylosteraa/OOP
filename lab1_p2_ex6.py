class BINARY_TREE:
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        if self.code:
            if code < self.code:
                if self.left is None:
                    self.left = BINARY_TREE(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = BINARY_TREE(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code
            self.price = price

    def find_code(self, code, quantity):
        if code < self.code:
            if self.left is None:
                return f'{code} is not Found'
            return self.left.find_code(code, quantity)
        elif code > self.code:
            if self.right is None:
                return f'{code} is not Found'
            return self.right.find_code(code, quantity)
        else:
            return self.price * quantity

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print("Product (", self.code, "): ", self.price)
        if self.right:
            self.right.print_tree()


product = BINARY_TREE(1564, 370)
product.insert(1256, 200)
product.insert(1287, 250)
product.insert(1298, 100)
product.insert(1258, 1000)
product.insert(1281, 450)
product.insert(1297, 350)

product.print_tree()
code = int(input("Enter the product code: "))
quantity = int(input("Enter the  number of products: "))
print(product.find_code(code, quantity))
