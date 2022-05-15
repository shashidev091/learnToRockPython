from functools import reduce

list_values = [2, 3, 5, 7, 4, 55]

evens = list(filter(lambda a: a % 2 == 0, list_values))

print(evens)

double_all = list(map(lambda a: a * 2, evens))
print(double_all)


reduce_all = reduce(lambda a, b: a + b, list_values)
print(reduce_all)


# decorators

ex_tuple = ('a',)
print(ex_tuple)


def function_one(msg):
    def inner_function(arg):
        arg = arg + ' Oye'
        return msg(arg)
    return inner_function


def normal_function(msg):
    return msg + ' !'


function_call = function_one(normal_function)
print(function_call("mango"))
