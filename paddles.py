from turtle import Turtle


class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.speed('fastest')

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

