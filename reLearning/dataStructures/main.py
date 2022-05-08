letters = ["a", "b", "c"]

print(letters)

items = [
    ("product1", 10),
    ("Product2", 20),
    ("product3", 30)
]

x = list(filter(lambda it: it[1] >= 10, items))
print(x)

for item in x:
    print(item)
    for product in item:
        print(product)
else:
    print("here")

list_items = []
for item in range(100):
    if item % 3 != 0 and item % 5 != 0:
        list_items.insert(-1, item)
else:
    print(list_items)
    print('loop end =======>')


''' Even numbers '''
prime_numbers = []

for item in range(100):
    if item % 2 == 0 and item != 0:
        prime_numbers.append(item)
else:
    print(prime_numbers)


for item in range(5):
    for i in range(item):
        print("#", end=' ')
    print('')


for item in range(5):
    for i in range(5 - item):
        print("#", end=' ')
    print('')
