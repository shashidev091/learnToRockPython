import random


def love_calculator():
    array_of = [input('Enter your name here \n').lower(), input('Enter him/her name \n').lower()]
    true_love = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']

    total = [0, 0]
    iterate = 0
    for elem in array_of:
        for item in true_love:
            if elem.count(item) > 0:
                print(elem.count(item))
                total[iterate] += elem.count(item)

        iterate += 1
    print(f'{total[0]}{total[1]}%')


# love_calculator()

'''
    Randomization 
'''

# random_integer = random.randint(0, 10)
# print(random_integer)


def tosh_a_coin():
    output = random.randint(0, 1)

    if output == 1:
        print('Heads')
    else:
        print('Tails')


# tosh_a_coin()

"""
    Lists
    - append() is used to add items in the list
    - extends() function is used to add another list or append an entire new list
"""

list_of_names = []


def add_items_inside_the_list():
    for item in range(1, 10):
        list_of_names.append(f'{item}')


# add_items_inside_the_list()

# print(list_of_names)

'''
    - Add the name of the people and the function will choose and give a random name who will be selected
'''


def guess_who_will_pay(names):
    random_index = random.randint(0, len(names) - 1)
    print(names[random_index])

    participants_names = input('Enter peoples name who will be participating followed by comma \n')
    if participants_names != '':
        list_names = participants_names.replace(' ', '').split(',')
        random_person = random.randint(0, len(list_names) - 1)
        print(f'{names[random_person]} will be paying for today')


# guess_who_will_pay(["Shashi", "Bhushan", "Bhagat"])


