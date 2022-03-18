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
# with open('testFile.txt', mode='w') as file:
#     file.write('Hello Shashi')


"""
    - Challenge to replace the name to the users you want from a text file
"""

with open('testFile.txt', mode='r') as file:
    content = file.read()
    print(content)


def write_love_letters():
    """
        This function writes love letters to multiple girls
        which names are present in \n
        names.txt file \n
        you can add or remove any name in it before running
    """
    with open('./names.txt', mode='r') as files:
        name_list = file.readlines()
        stripped_name = []
        for name in name_list:
            stripped_name.append(name.strip())

        with open('testFile.txt', mode='r') as letter:
            letter_content = letter.read()

        for girl_name in stripped_name:
            new_letter = letter_content.replace('[name]', girl_name)
            with open(f'./love_letters/{girl_name}.txt', mode='w') as love_letter:
                love_letter.write(new_letter)


write_love_letters()
