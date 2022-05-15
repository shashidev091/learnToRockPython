

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def add_all(*args):
    total = 0
    for item in args[0]:
        total += item
    return total


class Computer:
    author = "Shashi Bhagat"

    def __init__(self, motherboard, cpu, ram, brand, model, price):
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.laptop = self.Laptop(brand, model, price)

    def __str__(self):
        print(f"motherboard => {self.motherboard}, cpu => {self.cpu}, ram => {self.ram}")

    def config(self):
        print(f'{self.cpu} and {self.motherboard}')

    @classmethod
    def info(cls):
        return " " + cls.author

    class Laptop:
        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price

        def show(self):
            print(f"brand: {self.brand}\n model: {self.model}\n price: {self.price}")