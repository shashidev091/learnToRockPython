from turtle import Turtle, Screen


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def calculate(num1, num2, func):
    return func(num1, num2)


total = calculate(10, 20, add)
print(total)

my_turtle = Turtle()


def move_right():
    my_turtle.setheading(0)
    my_turtle.forward(50)


def move_left():
    my_turtle.setheading(0)
    my_turtle.setheading(180)
    my_turtle.forward(50)


def move_down():
    my_turtle.setheading(0)
    my_turtle.setheading(-90)
    my_turtle.forward(50)


def move_up():
    my_turtle.setheading(0)
    my_turtle.setheading(90)
    my_turtle.forward(50)


my_screen = Screen()
my_screen.listen()
my_screen.onkey(move_up, 'w')
my_screen.onkey(move_left, 'a')
my_screen.onkey(move_down, 's')
my_screen.onkey(move_right, 'd')
my_screen.exitonclick()
