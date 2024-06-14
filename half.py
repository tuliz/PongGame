from turtle import Turtle
class Half(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.width(5)
        self.goto(0,300)
        self.setheading(270)

    def create_half(self):
        for n in range(30):
            if n % 2 == 0:
                self.pendown()
            else:
                self.penup()

            self.forward(20)
