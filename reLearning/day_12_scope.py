from random import randint

"""
    - Python does not support block scope
    - use global scope for constants according to best practices
"""
external_variable = 10

# def function():
#     external_variable = 20
#     print(external_variable)


# function()

# print(external_variable)

"""
    - exercise
"""

lives_left = 5
guess_number = randint(1, 100)


def guess_game():
    global lives_left

    print(f'You have {lives_left} attempts left!!!')
    print(guess_number)
    if lives_left < 3:
        print(f'\033[93mHINT: The number is between '
              f'{guess_number - randint(1, 10) if guess_number > 10 else guess_number - 1} '
              f' and {guess_number + randint(1, 10) if guess_number < 100 else guess_number + 1}')

    lives_left -= 1
    guessed_number = int(input('Make a guess\n'))

    if guessed_number == guess_number:
        print(f'\033[92m <== Yea!!! your guess is absolutely right. The {guessed_number} is absolutely right... ==>')
    elif lives_left == 0:
        print('\033[91mYou have accede your limits... you lost 😜')
        print(f'The number I was thinking was {guess_number}')
    elif lives_left > 0:
        guess_game()
    else:
        print('You lost')


# guess_game()

"""
    - Debug fizz buzz
"""


def fizzbuzz(numbers):
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


# fizzbuzz([1, 5, 8, 99, 33, 65, 15])


"""
    - Coffee machine
"""

MENU = {
    "Expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            'milk': 100
        },
        "cost": 3.0
    }
}

resources = {
    "milk": 300,
    "water": 200,
    "coffee": 100
}


def sell_coffee():
    print("""
    Welcome to the coffee shop
            1- Expresso
            2- Latte
            3- Cappuccino'
    Please select from the list above
    """)

    choice_of_coffee = int(input('Choose the coffee from the list above\n'))
    type_of_money = input("How are you going to pay")


is_on = True


def coffee_machine():
    global is_on
    while is_on:
        choice = input('What would you like? (expresso/latte/cappuccino): \n').lower()
        if choice == 'off':
            is_on = False
            print('Machine off')
        elif choice == 'report':
            print(f"milk: \t {resources['milk']}")
            print(f"Water: \t {resources['water']}")
            print(f"coffee:  {resources['coffee']}")
        elif choice == '':
            print('You have to enter a valid ')


coffee_machine()
