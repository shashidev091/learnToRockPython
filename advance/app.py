# Classes in python
class Point:
    def draw(self):
        print("draw")


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
"""