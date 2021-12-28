import math
print('Hello Shashi')

print('*' * 12)

# formated stirng

strs = f"Shashi is learning python"

print(strs)
print(len(strs))
print(strs.capitalize())
print(strs.upper())
print(strs.find('S'))
print('Sh' in strs)
print(strs.replace('Shashi', "Shashi Bhushan"))

print(round(2.9))
print(math.ceil(2.2))
print(bool(5))
print(bool(0))
print(bool("False"))

temperature = 10

if temperature < 5:
    print('Temperature is low')
    print(f'Temperature is below {temperature}')
elif temperature == 10:
    print(f'Temperature is exactly same as {temperature}')
else:
    print("amazing")

# Ternary Operator in python
# and or not => These are logical operators
a = 11
mini = a if a > 10 else 0

print(mini)

# b = input('Enter something\n')
# print(b)

# for loops in python

for number in range(3):
    print('Say my name', number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print('Say my name', number, number * ".")

successful = True
for number in range(3):
    print("Attempts")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# find even numbers
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"we have {count} even numbers.")
