"""
    we use from for folder and import the attribute from the module
    keyword, module name, keyword, Thing in module
    from        turtle      import      Turtle
"""

"""
    - alias imports
    - import tutle as tur
"""


def add(*args):
    total = 0
    for item in args:
        total += item

    print(total)


add(1, 3, 5, 6, 3)


def kwargs_(**kwargs):
    print(kwargs['a'])
    print(kwargs.get('name'))


kwargs_(a=1, b=10, name="Shashi")
