"""
    - Dictionaries
"""

dict_people = {
    "Shashi": "FullStack Developer",
    "Stack": ["MEAN", "MERN", "PERN", "PDRP"]
}

print(dict_people["Stack"])

# Find frequency of each character

dictionaries_character = {}


def find_frequency(input_text):
    for char in input_text:
        if char in dictionaries_character:
            dictionaries_character[f"{char}"] += 1
        else:
            dictionaries_character[char] = 1
    print(dictionaries_character)


find_frequency("This world is awsome")

for item in dictionaries_character:
    print(f'{item} => {dictionaries_character}')
