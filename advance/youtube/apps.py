"""
    - building a guessing game
"""
import sys
import time
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


# create a car game
# Learn about the loader below

"""
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor


    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    
    - car game
"""

command = ''
previous_command = ''
engine_on = False

while True:
    command = input("> ").lower()
    if command == 'start':
        if not engine_on and previous_command != 'start':
            engine_on = True
            print('engine started')
        else:
            print("engine is already started")
    elif command == 'forward' and engine_on:
        print("Car is moving forward...")
    elif command == 'back' and engine_on:
        print("Car is going reverse")
    elif command == 'stop':
        if previous_command == command or not engine_on:
            print('car is already stopped.')
        elif engine_on:
            print("Car stopped moving")
            engine_on = False
    elif command == 'quit':
        print("You existed from the game.")
        break
    elif command == 'menu':
        print("""
start - to start the car
stop - to stop the car
forward - to accelerate the car
back - to reverse the car
turn off - to turn off the engine
quit - to exit the game
        """)
    else:
        print("I didn't understand the input")
    previous_command = command


print([0, [1, 2, 3, 4, 5][2], 2][1])
# output will be => 3


