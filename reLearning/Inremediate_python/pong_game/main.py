from turtle import Screen
from paddle import Paddle

pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.title("Pong Game")
pong_screen.bgcolor('#000')
pong_screen.tracer(0)
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
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
    pong_screen.update()


pong_screen.exitonclick()
