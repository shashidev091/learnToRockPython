from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        # self.write(f"Score : {self.score}", True, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

