# file = open('text_file.txt')
# content = file.read()
# print(content)

author = "Shashi Bhushan Bhagat"

# this closes the file when the file detects it work has been done
with open('text_file.txt') as file:
    contents = file.read()
    print(contents)

'''
    - To write into the file 
'''

with open('text_file.txt', mode='w') as file:
    file.write(f'''This world is amazing, and I will live to the fullest...
        And I {author} will be ruling this IT industry with my skills....
''')


"""
    - To append something inside the already existing file 
    - we need to use mode='a' since it means append
"""

with open('text_file.txt', mode='a') as file:
    file.write(f'\n \t\t I am {author}, and I am very nice guy loved by everyone')

# Challenge
with open('testFile.txt', mode='w') as file:
    file.write('Hello Shashi')
