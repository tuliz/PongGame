import random
from turtle import Turtle
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(0.7)

    def restart(self):
        self.goto(0,0)
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(180)
        else:
            self.setheading(0)

    def move(self):
        self.forward(20)

    def change_direction(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(random.randint(275, 360))

        else:
            self.setheading(random.randint(95, 260))
