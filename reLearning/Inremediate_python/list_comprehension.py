import random
# import pandas

list_numbers = [1, 3, 5, 6, 78, 3, 5, 55]
new_list = [n + 10 for n in list_numbers]
# print(new_list)

names = "Shashi"
new_names = [(name, f"{name}name") for name in names]
# print(new_names)

new_range_value = [item * 2 for item in range(1, 5)]
# print(new_range_value)

list_of_random_numbers = [random.randint(1, 100) for number in range(1, 10)]
# print(list_of_random_numbers)

prime_numbers = [prime_number for prime_number in list_of_random_numbers if prime_number % 2 == 0]
# print(prime_numbers)

# file_one_data = pandas.read_csv('file1.txt')
# print(file_one_data)

stripped_numbers = []
stripped_numbers_two = []
with open('file1.txt', 'r') as file_one:
    list_numbers = file_one.readlines()
    for item in list_numbers:
        stripped_numbers.append(int(item.strip()))

with open('file2.txt', 'r') as file_two:
    numbers = file_two.readlines()
    for item in numbers:
        stripped_numbers_two.append(int(item.strip()))


print(len(stripped_numbers), len(stripped_numbers_two))

# for index, item in enumerate(stripped_numbers):
#     if item in stripped_numbers_two:
#         common_items.append(item)

common_items = [item for item in stripped_numbers if item in stripped_numbers_two]

print(common_items)
