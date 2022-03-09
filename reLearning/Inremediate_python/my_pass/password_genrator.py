from string import ascii_uppercase, ascii_lowercase, digits
from random import randint

alphabets_lower = list(ascii_lowercase)
alphabets_caps = list(ascii_uppercase)
numbers = list(digits)
symbols = list("!@#$%^&*()_|?/,.\\")

list_of_items = [alphabets_caps, alphabets_lower, numbers, symbols]


def generate_random_password(length=8):
    random_password = ""
    for item in range(0, length):
        random_item = randint(0, 3)
        random_password += list_of_items[random_item][randint(0, len(list_of_items[random_item]) - 1)]
    return random_password
