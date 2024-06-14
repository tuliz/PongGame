from turtle import Turtle, Screen


class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.speed('fastest')
        self.screen = Screen()

    def build_paddles(self, x, y):
        for n in range(4):
            new_part = Turtle('square')
            new_part.color("white")
            new_part.shape("square")
            new_part.penup()
            new_part.width(20)
            if n == 0:
                new_part.goto(x,y)
            else:
                new_part.goto(self.parts[n-1].xcor(), self.parts[n-1].ycor() - 20)

            self.parts.append(new_part)

    def move_up(self):
        if self.parts[0].heading != 90:
            for part in self.parts:
                part.setheading(90)
                part.forward(10)
            self.screen.update()

    def move_down(self):
        if self.parts[0].heading != 270:
            for part in self.parts:
                part.setheading(270)
                part.forward(10)
            self.screen.update()

