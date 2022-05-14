# from array import *
from numpy import *

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
