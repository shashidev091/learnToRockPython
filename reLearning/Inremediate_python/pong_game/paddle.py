from turtle import Turtle
PADDLE_COLOR = "#fff"
PADDLE_SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddles = []
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(PADDLE_COLOR)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

