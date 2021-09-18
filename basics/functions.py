def greet():
    print('This is how function is defined.')
    print("You need to give 2 lines indent for next functions")


greet()


def greet_params(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet_params("Shashi", "Bhagat")


def greet_with_return(first_name, last_name):
    return f"Hi {first_name} {last_name}"


print(greet_with_return("Shashi", "Bhagat"))

# By default all functions return none

# keywords arguments are used for better readability
greet_params(first_name="Rabita", last_name="Bhagat")


def default_arguments(number, multiply_by=1):
    return number * multiply_by


result = default_arguments(10)
print(result)
result = default_arguments(number=10, multiply_by=20)
print(result)


# xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 5))


# xxargs
def save_users(**users):
    return users


res = save_users(id=1, name="Shashi", role="Admin")
print(res["name"])

# Change or modify a global variable from function
# Changing or modifying a global variable is said to be a bad practice since it may add bugs in out code
global_variable = 'original value'


def modify_global():
    global global_variable
    global_variable = 'new value'


modify_global()
print(global_variable)


# Exercise
# FizzBuzz problem


def find_fizz_buzz(input_value):
    return_value = input_value
    if input_value % 3 == 0 or input_value % 5 == 0:
        return_value = ""
        if input_value % 3 == 0:
            return_value += "fizz"
        if input_value % 5 == 0:
            return_value += "buzz"
    return return_value


fizzbuzz = find_fizz_buzz(7)
print(fizzbuzz)
