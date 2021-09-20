try:
    age = int(input("Enter your age : \n"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print(error)
else:
    print("No exceptions were thrown")


"""
    - Open a file
    - finally clause
"""

try:
    file = open("app.py")
    print(file)
except FileNotFoundError as e:
    print(e)
finally:
    file.close()

try:
    with open("app.py") as file:
        print("file Opened")
    print(file)
except FileNotFoundError as e:
    print(e)

"""
    - custom errors raising
    - raise keyword is used to throw/raise an exception
"""


def calculate(ages):
    if ages <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate(-3)
except ValueError as error:
    print(error)
