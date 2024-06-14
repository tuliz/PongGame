from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed('fastest')
        self.penup()
        self.hideturtle()

    def create_score(self):
        self.write(f"{self.score}", align='center',font=('Times',50,'bold'))

