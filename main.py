from turtle import Screen
from paddles import Paddles
from pong import Pong
from scoreboard import Scoreboard
screen = Screen()
screen.screensize(400,400)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(1)
screen.listen()
pc = Paddles()
pc.goto(-360,0)
player = Paddles()
player.goto(360,0)
pc_score = Scoreboard()
player_score = Scoreboard()
ball = Pong()



screen.exitonclick()

