from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_cors = 1
        self.y_cors = 1

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.color('salmon')
        # self.goto(0, 0)
        # self.setheading(30)

    def move(self):
        x_cors = self.xcor() + self.x_cors
        y_cors = self.ycor() + self.y_cors
        self.goto(x_cors, y_cors)

    def bounce_x(self):
        self.x_cors *= -1

    def bounce_y(self):
        self.y_cors *= -1
