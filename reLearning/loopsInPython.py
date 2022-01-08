list_fruits = ['🍎', '🥭', '🍊', '🍌']

# for fruit in list_fruits:
#     print(fruit)


def find_average_height(list_heights):
    temp = 0
    for height in list_heights:
        temp += height
    average_height = temp / len(list_heights)
    print(f'Average height is {round(average_height)}')
    print(sum(list_heights) // len(list_heights))


# find_average_height([180, 124, 165, 173, 189, 169, 146])


def find_max(list_numbers):
    maximum = list_numbers[0]
    for number in list_numbers:
        if number > maximum:
            maximum = number

    print(f'The maximum number in the list is {maximum}')
    print(max(list_numbers))


# find_max([78, 65, 89, 55, 91, 64, 89])


def calculate_all_evens(type_of):
    total_evens = 0
    if type_of == 1:
        for number in range(0, 101):
            if number % 2 == 0:
                total_evens += number

    else:
        for number in range(2, 101, 2):
            total_evens += number

    print(total_evens)


# calculate_all_evens(1)


def fizzbuzz():
    for item in range(1, 101):
        if item % 3 == 0 and item % 5 == 0:
            print('fizzBuzz')
        elif item % 3 == 0:
            print('fizz')
        elif item % 5 == 0:
            print('buzz')


# fizzbuzz()


'''
    - Make a password generator
'''
