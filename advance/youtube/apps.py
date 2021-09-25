"""
    - building a guessing game
"""
from random import randint

print("Game starts here")


guess_limit = 3
guess_count = 0
guess_number = randint(0, 9)
print(guess_number)


def guessing_game(input_value):
    global guess_count
    if input_value == guess_number:
        print('🎉 You won the game🎉 \n👏you are a good guesser 👏')
        return True
    elif guess_count < 2:
        print('please try again &')


while guess_count < guess_limit:
    guessed_number = int(input("enter the number\n"))
    found = guessing_game(guessed_number)
    if found:
        break
    guess_count += 1
else:
    print("All your guesses are wrong.")

"""
    - while loops can also have else part
"""