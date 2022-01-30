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
    global index
    index += 1
    all_bid[name] = bid_amount
    print(all_bid)

    is_more_entry = input('Do you want to enter more bids \n')

    if is_more_entry == 'yes':
        find_biggest_bid()
    else:
        list_of_bids = 0
        winner = ''
        for bid in all_bid:
            if all_bid[bid] > list_of_bids:
                list_of_bids = all_bid[bid]
                winner = bid

        print(f'The highest bid is {list_of_bids} by {winner}')


# find_biggest_bid()


def formate_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


# print(formate_name("SHASHI", "Bhagat"))

