# Classes in python
class Point:
    def draw(self):
        apple = "apple"
        self.print_something(apple)

    def print_something(self, a):
        return "Yahoo" + a


point = Point()
print(type(point))
isinstance(point, Point)

point.draw()

"""
    - Creating constructor
"""


class MyPoint:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x


my_point = MyPoint(1, 3)

print(my_point.get_x())
my_point.default_color = "green"

"""
    - changes made to class level variables with an object is not inherited with other instances
    - but changes made by class reference it gets inherited in all instances 
"""
print(my_point.default_color)
print(MyPoint.default_color)

"""
    - factory method => method declared in class level
"""


class Factory:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)


factory = Factory.zero()
print(factory.x, factory.y)

"""
    - magic methods
    - they are called automatically by python compiler
"""


class MagicMethods:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a}, {self.b})"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b

    def __add__(self, other):
        return MagicMethods(self.a + other.a, self.b + other.b)


magic = MagicMethods(4, 5)
others = MagicMethods(4, 5)
other_gt = MagicMethods(5, 6)
print(str(magic))
print(magic)

print(magic == others)
print(other_gt > others)


"""
    - Performing arithmetic operations using magic functions
"""

combined = others + other_gt
print(combined.b)


"""
    - Making custom containers
"""


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("mango")

print(len(cloud))

"""
    - all the classes have __dict__
    - it holds all the attributes of the class
    - Python does not have concept of private members
"""

# print(cloud.__dict__)
# print(cloud._TagCloud__tags)


"""
    - properties
    - how can you make your class level variables non negative
"""


class PropertiesClass:
    def __init__(self, value):
        self.price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


propertyClass = PropertiesClass(10)
print(propertyClass.price)
# propertyClass.price = 20
print(propertyClass.price)


"""
    * Inheritance
    * overloading
"""


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 10

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
mammal.eat()
mammal.walk()
print(mammal.age)


"""
    - Useful builtin functions
    - object call is parent of all classes
"""

print(isinstance(mammal, Animal))
print(isinstance(mammal, object))
print(issubclass(Mammal, object))
