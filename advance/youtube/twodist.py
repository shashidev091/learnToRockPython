matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

for row in matrix:
    for item in row:
        if item == 5:
            item = 10
        print(item, end=', ')
    print('\n')

