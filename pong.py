import random
from turtle import Turtle
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(0.7)
        self.x_movement = 20
        self.y_movement = 20

    def restart(self):
        self.goto(0,0)
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(random.randint(95, 260))
        else:
            self.setheading(random.randint(275, 360))

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x,new_y)
    def hit_paddle(self):
        #if self.heading() > 90 and self.heading() < 270:
            #self.setheading(random.randint(275, 360))
        self.x_movement *= -1
        #else:
            #self.setheading(random.randint(95, 260))

    def bounce(self):
        self.y_movement *= -1