import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.onkey(snake.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # if segments[0].xcor() > 290 or segments[0].ycor() > 290 or segments[0].ycor() < -290 or segments[0].xcor() < -290:
    #     segments[0].right(90)

screen.exitonclick()
