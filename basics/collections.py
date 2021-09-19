from array import array

array_of_numbers = array("i", [1, 2, 3, 4, 5])
print(array_of_numbers[0])


"""
    (0) sets
    - to remove duplicates we use sets because it returns only unique values
    - we use {} do define sets
    - sets cannot be accessed using indexes
"""

numbers = [1, 2, 5, 5, 3, 5, 7, 4, 24, 2, 4, 63, 23, 4, 25, 23, 32]
print("normal list with duplicate items", numbers)

unique = set(numbers)
print("with only unique value", unique)

# get union of two sets
set_one = {1, 4, 6, 8}
set_two = {1, 5, 6, 9}

print("This set only all the values from both set with unique values \n", set_one | set_two)

# intersection => all item which is common on both items
print("common on both sets\n", set_one & set_two)

# find elements which are present in second element
print(set_one - set_two)

# symmetric difference => items which are not common
print(set_one ^ set_two)

"""
    Dictionaries
    - its a key value pair objects
    - we use immutable kind of things for declaring keys 
    - dict() can be used to create dictionaries 
    - we access dictionaries by using keys
"""

dict_one = {"x": 1, "y": 2}

dict_two = dict(x=1, y=2)

# fetching values
print(dict_one["x"])

# always check before fetching the item or it will throw error
# or you can use the get() it return "None" if data not found
if "a" in dict_one:
    print(dict_one["a"])

print(dict_one.get('a'))

# you can also add a default value if key not found
print(dict_two.get("a", "not found"))

# to delete we use "del" keyword
del dict_one['x']

print(dict_one)

# loop in dictionary
for key in dict_two:
    print(key)

# to print key with values
for key in dict_two:
    print(key, dict_two[key])

# or use dict.items() it gives tuple on each iterations
for key, value in dict_two.items():
    print(key, value)

"""
    - dictionary comprehension
"""

# [expression for item in items]
output = {x: x * 2 for x in range(5)}
print(output)

print({dict_two[x] for x in dict_two})
print({x for x in dict_two.items()})

"""
    => Generators and Unpacking
"""
# this returns an generator object, they can be iterated
val = (x for x in dict_two.items())

for x in val:
    print(x)

# unpacking with * for list and "**" for dictionaries
gen_list = [item for item in (x for x in dict_two.items())]
print(*gen_list)

dict_three = dict(a=10, b=20)
print({**dict_one, **dict_two, **dict_three})

"""
    - Exercise
    - find the most repeated string
"""

sentence = "This is a common interview question"

sequence = {}
for item in sentence:
    if item in sequence:
        sequence[item] += 1
    else:
        sequence[item] = 1

sorted_list = sorted(sequence.items(), key=lambda items: items[1], reverse=True)
print(sorted_list[0])
