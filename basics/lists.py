from collections import deque
numbers_list = list(range(20))
print(numbers_list)

list_of_string = ["apple", "mango", "banana"]
print(list_of_string)
print(numbers_list[0:5])
print(numbers_list[:10])
print(numbers_list[:])
print(numbers_list[::2])
print(numbers_list[::-1])
print(list_of_string[::-1])

# Unpacking lists
first, second, third = list_of_string
print(first, second, third)

a, *others = list_of_string
print(a, others)

# to get the first and last element and the others remaining in the list
f, *other_remaining, last = numbers_list
print(f, other_remaining, last)

# Traversing or iterating a list
fruits = ["apple", "banana", "cranberry", "dates", "elderberries", "figs", "grapes", "honey melon"]
for fruit in fruits:
    print(fruit)

# To print with indexes we can use enumeration
# in each iteration enumerate returns a tuple
for fruit in enumerate(fruits):
    print(fruit)

# to unpack the enumerated object or tuple we can unpack same as lists
for index, fruit in enumerate(fruits):
    print(index, fruit)

# add item in the end of the list
fruits.append("java-plum")
print(fruits)

# add item at particular index
fruits.insert(6, "jujube fruit")
print(fruits)

# Remove item from the end of the list
fruits.pop()
print(fruits)

# Remove item form any desired index that exists
fruits.pop(6)
print(fruits)

# Remove item of which you don't know the index
if "cranberry" in fruits:
    fruits.remove("cranberry")
print(fruits)

# Remove a range of items from the list
del fruits[: 4]
print(fruits)

# to get the numbers of occurrence in the list
print(fruits.count("figs"))

# You can find the index of any element in the list
print(fruits.index('figs'))

"""
    Sorting list in Python
    - using sort() alters the original list
    - where as predefines method sorted() does not
"""
fruits.sort(reverse=True)
print(fruits)

sorted(list_of_string)
print(list_of_string)

"""
    # Sort a list of tuples
"""

products = [
    ("Product_1", 10),
    ("Product_2", 9),
    ("Product_3", 22)
]

print(products)

for product_name, product_price in products:
    print(f"Product {product_name} is of {product_price}")

# sort according to the price of the product

products.sort(key=lambda item: item[1])
print(products)

products.sort(key=lambda item: item[1], reverse=True)
print(products)

"""
    - map function
    - filter function
"""

x = map(lambda item: item[1], products)
print(x)
print(list(x))


filtered = filter(lambda item: item[1] > 10, products)
print(list(filtered))


"""
    - Comprehension
    - zip()
"""

mapped = [product[1] * 10 for product in products]
print(mapped)

filtered = [product for product in products if product[1] > 10]
print(filtered)

"""
    - Queue and de-queue
"""

queue_list = deque([])
queue_list.append(1)
queue_list.append(2)
queue_list.append(3)

print(queue_list)
# remove item from the beginning
queue_list.popleft()
print(queue_list)

if not queue_list:
    print('Empty')
else:
    print(len(queue_list))

"""
    => Tuples
    - tuples are immutable iterable objects
    - tuple is read-only so we do not have any add or remove methods
    - we can concat two tuples
    - similar to lists we can get items using indexes
    - we can check tuples using "in" operator
"""

point = (1, 3, 4)
print(point)

concat_tuple = point + (5, 6, 7)
print(concat_tuple)

# we can declare tuple without the parenthesis also
# but if there is only one item then it should end with , so that compiler doesn't get confused
without_parenthesis = 1,
print(without_parenthesis)

if 6 in concat_tuple:
    print("yes it exists")

# Swap values

a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)

# we can swap very easily in python by using tuples

a, b = b, a
print(a, b)
