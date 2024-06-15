from turtle import Turtle, Screen


class Paddles(Turtle):
    def __init__(self, location):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(location)
        self.setheading(90)
        self.shapesize(stretch_wid=1,stretch_len=7)
        self.screen = Screen()


    def move_up(self):
        if self.heading != 90 and self.ycor() < 305:
            self.setheading(90)
            self.forward(20)
            self.screen.update()

    def move_down(self):
        if self.heading != 270 and self.ycor() > -300:
            self.setheading(270)
            self.forward(20)
            self.screen.update()

