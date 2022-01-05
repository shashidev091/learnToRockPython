import math
from datetime import date


def add_new_patient():
    person_name = input('Enter you name\n')
    person_age = input('Enter you age\n')
    person_response = input('Have you been here?\n')

    is_new = False

    print(person_response == "yes")

    if not is_new:
        print(f"Person name is {person_name} and he is {person_age} years old.")
        print('He is a new patient')
    else:
        print(f"Patient named {person_name} is an old patient..")


def convert_lbs_to_pound():
    weight_in_lbs = input('Enter your weight\n')
    weight_in_kg = float(weight_in_lbs) // 2.2046
    print(f'your weight is {int(weight_in_kg)}KG')


# convert_lbs_to_pound()

something = '''I love this world and the world loves me'''

# print(len(something))  # length function
# print(something.replace('world', 'world'.upper()))
# print(something.find('world'))

# x = 10
# x += 1
# print(x)

'''
    Math functions
'''

x = 234.34
# print(abs(-2.9), 'returns only positive values')
# print(round(2.9), 'returns the round off of given number')
#
# print(math.ceil(2.9), 'will return the next possible value')
# print(math.floor(2.9), 'will return the least value')

'''
    Problem number => 3
'''


def down_payment_required():
    price = 1000000
    credit = input('Enter you credit score\n')
    if int(credit) > 750:
        down_payment = 0.1 * price
        print(f'you need to pay 10% down payment')
    else:
        down_payment = 0.2 * price
        print('You need to pay 20% down payment')

    print(f'Your payable down payment is {down_payment}')


# down_payment_required()


def loan_eligibility_checker():
    income = input('Enter you income\n > ')
    credit_score = input('Enter you credit score\n > ')

    if int(income) > 1000000 and int(credit_score) > 750:
        print('you are eligible for the loan')
        print('Since your credit score is quite good you are eligible for the loan')
    else:
        print('Sorry to say that you are not eligible for the loan')


# loan_eligibility_checker()

img_prices = [10, 20, 30]
totals = 0
for item in img_prices:
    totals += item
# print(totals)


pattern = [5, 2, 5, 2, 2]

# for ele in pattern:
#   print('#' * ele)

lists = ['John', 'Bob', 'Sarah']

# print(lists)
lists[0] = 'Shashi'


# print(lists)


def largest_number(list_of_numbers):
    maximum = list_of_numbers[0]
    minimum = list_of_numbers[0]
    for element in list_of_numbers:
        if minimum > element:
            minimum = element
        elif maximum < element:
            maximum = element

    print(f'maximum => {maximum} ', f' minimum => {minimum}')


arrays = [1, 4, 6, 23, 7, 122, 7788, 2, 0]
# print(arrays[0])
# largest_number(arrays)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    rows = ''
    for ele in row:
        rows += str(ele) + ' '

    # print(rows)


def sort_list():
    # global arrays
    for i in range(len(arrays)):
        for j in range(i + 1, len(arrays)):
            if arrays[i] > arrays[j]:
                # now swap the elements
                temp = arrays[i]
                arrays[i] = arrays[j]
                arrays[j] = temp

    # print(arrays)


# sort_list()

# Remove duplicates from the list


def remove_duplicates(list_numbers):
    temp_list = []
    for i in list_numbers:
        if i not in temp_list:
            temp_list.append(i)
    print(list_numbers)
    print(temp_list)


# remove_duplicates([1, 33, 6, 33, 4, 7, 3, 1, 99, 3, 5, 4])

'''
    # Tuples => are immutables
'''


# print('Hello ' + input('What is your name... \n'))

# print(len('Angela'))


def generate_band_name():
    city = input("What's name of the city you grew up in...???\n")
    pet_name = input("What's your pet's name\n")

    print(f"Your band name could be {city} {pet_name}")


# generate_band_name()

# find number of digits avalable
# print(len(str(2342342342)))
# print('Hello'[-1])


def bmi_calculator():
    weight = input('Enter your weight \n')
    height = input('Enter your height \n')

    print(f"Your BMI is {round(int(weight) / (float(height) ** 2))}")


# bmi_calculator()


def calculate_no_of_days_remaining():
    dob = input('Enter your date of birth in dd/mm/yy format \n')
    extract = dob.split('/')
    list_of_date = list(map(int, extract))

    year = date.today().year
    month = date.today().month
    day = date.today().day

    print(f'{str(day).zfill(2)}/{str(month).zfill(2)}/{year}')

    remaining = date(list_of_date[2] + 90, list_of_date[1], list_of_date[0]) - date(year, month, day)
    print(remaining)


# calculate_no_of_days_remaining()

'''
    Tip calculator app
'''


def tip_calculator():
    total_amount = float(input("Enter the total bill of the order \n"))
    tip_percentage_you_want_to_pay = int(input("Enter the % of the tip you wanna pay.. \n"))
    total_no_of_people = int(input("Total no of people you want to split your bill into \n"))

    if tip_percentage_you_want_to_pay < 10:
        print("Tip cannot be less than 10% ")
        tip_calculator()
    else:
        percentage_amount = total_amount / 100 * tip_percentage_you_want_to_pay
        total_bill = total_amount + percentage_amount
        for_each_person = total_bill / total_no_of_people

        print(f'The total bill amount is {total_bill}.\nEach person should pay ${":.2f".format(for_each_person)} 🥸')
        print(f"The rounded amount will be ${round(for_each_person, 2)} each. 🥸")


# tip_calculator()


'''
    Check odd or even
'''


def check_even_or_odd():
    inp = int(input("Enter the number to find out its even or odd \n"))

    if inp % 2 == 0:
        print(f'{inp} is an even number')
    else:
        print(f'{inp} is an odd number')


# check_even_or_odd()


'''
    roller coaster ticket counter
'''


def book_ticket():
    height = int(input("Enter your height in centimeters \n"))

    if height < 120:
        print('You are not eligible to ride this roller coaster...')
    else:
        age = int(input('Enter your age \n'))

        if age < 12:
            print('You have to pay $5')
        elif 12 <= age < 18:
            print('You have to pay $7')
        else:
            print('you have to pay $12')


# book_ticket()


def is_leap_year():
    year = int(input("Enter the year \n"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} this is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} this is not a leap year")


# is_leap_year()