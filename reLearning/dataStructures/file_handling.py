file = open('shashi.txt', 'r')

# print(file.read())

# data = file.read()readΩ

print(file.readline())

write_something = open('shashi.txt', 'w')

# first loop is used to copy data of the entire file
# and can be used to create a new file
for data in file:
    write_something.write(data)
else:
    write_something.write('\nThis is a great way to learn programming')

read_again = open('shashi.txt', 'r')

print(read_again.read())


def binary_search(list_, n):
    list_.sort()
    lower_bound = 0
    upper_bound = len(list_) - 1
    while lower_bound <= upper_bound:
        mid_bound = (lower_bound + upper_bound) // 2
        if list_[mid_bound] == n:
            return mid_bound
        else:
            if list_[mid_bound] < n:
                lower_bound = mid_bound + 1
            else:
                upper_bound = mid_bound - 1
    return -1


list_items = [1, 34, 45, 47, 47, 57, 57, 59, 9494, 949449, 10]

print(binary_search(list_items, 1))

