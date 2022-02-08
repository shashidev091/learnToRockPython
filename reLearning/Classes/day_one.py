import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.color('coral')
print(my_turtle)
turtle.forward(100)
turtle.right(90)
turtle.forward(90)
my_turtle.shape('turtle')

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

