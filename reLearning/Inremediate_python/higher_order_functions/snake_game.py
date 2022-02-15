import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    # Detect collision
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        scoreboard.add()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
