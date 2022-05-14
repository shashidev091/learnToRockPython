# from array import *
from numpy import *

# from os import system

# value = array('i', [1, 2, 4, 5, 6])
values = array([[1, 2, 4, 5, 6], [1, 34, 5, 4, 9]])

for item in values:
    print(item)


def add_sub(x, y):
    adds = x + y
    sub = x - y
    return adds, sub


result_add, result_sub = add_sub(10, 20)

print(result_add, result_sub)

global_variable = 10

'''
    you can access global variable but once you want to modify the variable you need to use "global" keyword
'''


def change_variable():
    # global global_variable
    global_variable = 20
    print(id(global_variable))
    return global_variable


print(change_variable())

print(global_variable, id(global_variable))

# system(command="clear")

list_of_emojis = ["🍎", "🥝", "🍉", "🫐", "🍓", "🍇"]

print(len(list_of_emojis))

for index, fruit in enumerate(list_of_emojis):
    print(index, fruit)

for item in zip(list_of_emojis, range(len(list_of_emojis))):
    print(item)


# fibonacci series

def print_fibonacci_series(till):
    a = 0
    b = 1
    print(a)
    print(b)
    for item in range(2, till):
        temp = a + b
        a = b
        b = temp
        print(temp)


print_fibonacci_series(10)


# factorial of a number


def find_factorial(value):
    factorial = 1
    for item_of in range(1, value + 1):
        factorial *= item_of
    return factorial


print("factorial of 4 is", find_factorial(4))

"""
    - find factorial using RECURSION
"""

factorial_value = 1
initial_value = 1


def find_factorial_recursion(value):
    if value > 0:
        global factorial_value, initial_value
        factorial_value *= initial_value
        initial_value += 1
        value -= 1
        find_factorial_recursion(value)


find_factorial_recursion(4)
print(factorial_value)


# optimised version


def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)


print(fact(4))
