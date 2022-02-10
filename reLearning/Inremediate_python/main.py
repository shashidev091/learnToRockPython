import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle_screen = Screen()

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


# for shape_side_no in range(3, 11):
#     my_turtle.color(random.choice(colors))
#     generic_shape(shape_side_no)

direction = [0, 90, 180, 270]
my_turtle.speed("fast")


def random_color():
    r = float(random.randint(0, 255))
    g = float(random.randint(0, 255))
    b = float(random.randint(0, 255))
    rgb = (r, g, b)
    return rgb


def random_walk():
    print(random_color())
    my_turtle.pensize(10)
    my_turtle.color(random.choice(colors))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))


# for _ in range(100):
#     random_walk()

my_turtle.speed("fastest")
# for _ in range(50):
#     my_turtle.circle(100)
#     my_turtle.forward(10)
#     my_turtle.right(10)
#
# my_turtle_screen.exitonclick()


# for _ in range(int(360 / 10)):
#     my_turtle.color(random.choice(colors))
#     my_turtle.circle(100)
#     my_turtle.setheading(my_turtle.heading() + 10)
#
# my_turtle_screen.exitonclick()

