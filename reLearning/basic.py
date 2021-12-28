import math


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

print(len(something))  # length function
print(something.replace('world', 'world'.upper()))
print(something.find('world'))

# x = 10
# x += 1
# print(x)

'''
    Math functions
'''

x = 234.34
print(abs(-2.9), 'returns only positive values')
print(round(2.9), 'returns the round off of given number')

print(math.ceil(2.9), 'will return the next possible value')
print(math.floor(2.9), 'will return the least value')

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
print(totals)


pattern = [5, 2, 5, 2, 2]

for ele in pattern:
    print('#' * ele)


