import random
from turtle import Turtle, Screen

colors = ["red", "orange", "purple", "yellow", "blue", "green"]
positions = [-100, -60, -20, 20, 60, 100]
# red_turtle = Turtle("turtle")
my_screen = Screen()
my_screen.setup(width=500, height=400)
#
# red_turtle.penup()
# red_turtle.goto(x=-230, y=-100)
# red_turtle.color(colors[0])
#
# orange_turtle = Turtle('turtle')
# orange_turtle.penup()
# orange_turtle.goto(x=-230, y=-50)
# orange_turtle.color(colors[1])
#
# purple_turtle = Turtle('turtle')
# purple_turtle.color(colors[2])
# purple_turtle.penup()
# purple_turtle.goto(x=-230, y=0)
#
# yellow_turtle = Turtle('turtle')
# yellow_turtle.penup()
# yellow_turtle.color(colors[5])
# yellow_turtle.goto(x=-230, y=50)
#
# blue_turtle = Turtle('turtle')
# blue_turtle.penup()
# blue_turtle.color(colors[4])
# blue_turtle.goto(x=-230, y=100)
all_turtles = []

for _ in range(6):
    my_turtle = Turtle('turtle')
    my_turtle.color(colors[_])
    my_turtle.penup()
    my_turtle.goto(x=-230, y=positions[_])
    all_turtles.append(my_turtle)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: \n")

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Yeaaa!!! you have won! {winning_color} turtle is the winner 🇮🇳")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                break
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()
