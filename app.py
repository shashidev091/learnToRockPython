import math
print('Hello Shashi')

print('*' * 12)

# formated stirng

strs = f"Shashi is learning pyhton"

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

b = input('Enter something\n')
print(b)
