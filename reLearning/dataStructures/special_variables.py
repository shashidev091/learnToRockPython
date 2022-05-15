from calculator import add_all

num_list = [1, 4, 564, 3, 23, 6]

print(add_all(num_list))


class Computer:
    author = "Shashi Bhagat"

    def __init__(self, motherboard, cpu, ram):
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.laptop = self.Laptop("Apple", "macbook pro 2022 16\"", 234234)

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
            print(f"brand: {self.brand}\nmodel: {self.model}\nprice: {self.price}")


comp = Computer('Asus', "intel", 4)
comp.config()

comp2 = Computer('gigabit', 'AMD', 16)

Computer.config(comp2)

comp.__str__()

print(Computer.author)
print(Computer.info())
comp2.laptop.show()
