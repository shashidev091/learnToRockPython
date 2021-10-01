myList = ["banana", "cherry", "apple"]
print(myList)

item = myList[0]
print(item)

for items in myList:
    print(items)

print(list(filter(lambda fruit: fruit == "banana", myList)))

print(sorted(myList))

myComplexList = [("name", "Shashi"), ("name", "Bhagat")]

print(myComplexList)

name = [names[1] for names in myComplexList]
print(name)

for name, item in myComplexList:
    print(name, item)

print(len(myComplexList))

for row in range(5):
    for col in range(1, 6):
        print(end=str(col))
    print('')


for row in range(5):
    for col in range(1, row + 1):
        print(end=str(col))
    print('')

print('\n')
rang = 5
for row in range(rang):
    for col in range(1, rang):
        print(end=str(col))
    print('')
    rang = rang - 1


"""
    1
    1 2
    1 2 3
    1 2 3 4 
    1 2 3 4 5
"""

for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=' ')
    print()

"""
    *
    * *
    * * *
    * * 
    *
"""

for row in range(5):
    print('* ' * row)
for row in range(5):
    print('* ' * (5 - row))

# for row in range(1, 6):
#     for col in range(row):
#         print('*', end=' ')
#     print()
# for row in range(1, 6):
#     for col in range(5 - row):
#         print('*', end=' ')
#     print()

for row in range(1, 12):
    if row < 11/2:
        for col in range(row):
            print('*', end=' ')
    else:
        for col in range(12 - row):
            print('*', end=' ')
    print()
