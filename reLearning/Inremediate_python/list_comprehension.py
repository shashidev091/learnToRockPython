import random

list_numbers = [1, 3, 5, 6, 78, 3, 5, 55]
new_list = [n + 10 for n in list_numbers]
print(new_list)

names = "Shashi"
new_names = [(name, f"{name}name") for name in names]
print(new_names)

new_range_value = [item * 2 for item in range(1, 5)]
print(new_range_value)

list_of_random_numbers = [random.randint(1, 100) for number in range(1, 10)]
print(list_of_random_numbers)

prime_numbers = [prime_number for prime_number in list_of_random_numbers if prime_number % 2 == 0]
print(prime_numbers)

