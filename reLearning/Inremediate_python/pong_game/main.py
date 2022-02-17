from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.title("Pong Game")
pong_screen.bgcolor('#000')
pong_screen.tracer(0)
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
game_is_on = True


def close_app():
    global game_is_on
    pong_screen.bgcolor('green')
    game_is_on = False


# pong_screen.update()
pong_screen.listen()
pong_screen.onkey(l_paddle.go_up, 'w')
pong_screen.onkey(l_paddle.go_down, 's')
pong_screen.onkey(r_paddle.go_up, 'Up')
pong_screen.onkey(r_paddle.go_down, 'Down')
pong_screen.onkey(close_app, 'p')


while game_is_on:
    # if ball.xcor() >= 230 or ball.ycor() > 230:
    #     ball.setheading(ball.heading() - 270)
    # if ball.xcor() <= -230 or ball.ycor() < -230:
    #     ball.setheading(ball.heading() + 270)
    # ball.forward(1)
    pong_screen.update()
    ball.move()

    # wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 330 or ball.distance(r_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 360 or ball.xcor() < -360:
        # close_app()
        ball.reset_position()

pong_screen.exitonclick()
