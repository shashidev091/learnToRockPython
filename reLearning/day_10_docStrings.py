"""
    - DocStrings
    - It's a string that shows what your function will do, or you want the user to know about it.
"""


def find_min_and_max(list_inp):
    """This will take a list as an input and produce min and max"""
    min_elem = list_inp[0]
    max_elem = list_inp[0]

    for element in list_inp:
        if element > max_elem:
            max_elem = element
        if element < min_elem:
            min_elem = element

    return f"minimum value is \"{min_elem}\" and the maximum value is \"{max_elem}\""


min_max = find_min_and_max([1, 4, 7, 2, 9, 6])
print(min_max)


"""
    - Calculator
"""


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operators = {
    '+': add,
    '-': sub,
    '/': divide,
    '*': multiply
}


num1 = int(input('What is the first number\n'))
num2 = int(input('What is the second number\n'))

for symbol in operators:
    print(symbol)

operation_symbol = input("Pick the operation from the list above: ")
calculation_function = operators[operation_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')
