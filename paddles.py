from turtle import Turtle
class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.width(20)
        self.speed('fast')

