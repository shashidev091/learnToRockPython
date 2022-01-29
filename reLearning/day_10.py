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


# find_frequency("This world is awsome")

# for item in dictionaries_character:
#     print(f'{item} => {dictionaries_character}')

all_bid = {}
index = 0


def find_biggest_bid():
    name = input('Enter your name \n')
    bid_amount = int(input('Enter the bid amount \n'))
    bid_list = [name, bid_amount]
    global index
    index += 1
    all_bid[f'Person {index}'] = bid_list
    print(all_bid)

    isMoreEntry = input('Do you want to enter more bids')

    if isMoreEntry == 'yes':
        find_biggest_bid()
    else:
        print(all_bid)


find_biggest_bid()
