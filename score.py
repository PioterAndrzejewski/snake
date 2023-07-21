from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.amount = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.write(f"Your score: {self.amount}", align="center")

    def add_point(self):
        self.amount += 1
        self.clear()
        self.write(f"Your score: {self.amount}", align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center")