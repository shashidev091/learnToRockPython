import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')

# temp_turtle = Turtle()

colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "SlateGray", "SeaGreen"]


def draw_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)
    # my_turtle.backward(200)

    screen = Screen()
    screen.exitonclick()


def draw_dashed_line():
    for _ in range(10):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()

    screen = Screen()
    screen.exitonclick()


# draw_dashed_line()

def generic_shape(no_sides):
    for _ in range(no_sides):
        angle = 360 / no_sides
        my_turtle.forward(100)
        my_turtle.right(angle)


for shape_side_no in range(3, 11):
    my_turtle.color(random.choice(colors))
    generic_shape(shape_side_no)
