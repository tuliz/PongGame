from turtle import Screen
from paddles import Paddles
from pong import Pong
from scoreboard import Scoreboard
from half import Half

#screen settings
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

#creating pc paddles
pc = Paddles()
pc.goto(-360, 0)
#creating player paddles
player = Paddles()
player.goto(360, 0)

#creating PC scoreboard
pc_score = Scoreboard()
pc_score.goto(-50,260)
pc_score.create_score()

#creating Player scoreboard
player_score = Scoreboard()
player_score.goto(50,260)
player_score.create_score()

ball = Pong()

half = Half()
half.create_half()

screen.update()



screen.exitonclick()
