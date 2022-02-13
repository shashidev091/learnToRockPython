import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

segments = []
for position in [(0, 0), (-20, 0), (-40, 0)]:
    turtle = Turtle("square")
    turtle.penup()
    turtle.color("white")
    turtle.goto(position)
    segments.append(turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    # if segments[0].xcor() > 290 or segments[0].ycor() > 290 or segments[0].ycor() < -290 or segments[0].xcor() < -290:
    #     segments[0].right(90)

screen.exitonclick()
