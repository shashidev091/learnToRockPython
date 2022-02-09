from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')

# temp_turtle = Turtle()


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


draw_dashed_line()

