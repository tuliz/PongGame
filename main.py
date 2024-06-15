from turtle import Screen
from paddles import Paddles
from pong import Pong
from scoreboard import Scoreboard
from half import Half
import time

#screen settings
screen = Screen()
screen.screensize(700,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#creating pc paddles
pc = Paddles((-350, 0))

#creating player paddles
player = Paddles((350, 0))

#creating PC scoreboard
pc_score = Scoreboard()
pc_score.goto(-50,250)
pc_score.create_score()

#creating Player scoreboard
player_score = Scoreboard()
player_score.goto(50,250)
player_score.create_score()

ball = Pong()

half = Half()
half.create_half()

game_continue = True

screen.update()

#listeners for paddles for moving it up and down
screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')
screen.onkey(pc.move_down, 's')
screen.onkey(pc.move_up, 'w')



while game_continue:

    ball.move()
    screen.update()
    time.sleep(0.1)

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    #checking if the ball is having a collision with one of the paddles, if yes change the ball direction
    if ball.distance(player) < 25 or ball.distance(pc) < 25:
        ball.hit_paddle()

    #checking if the ball is passing the pc side paddle, if yes up the score for player
    if ball.xcor() > 362:
        pc_score.score_up()
        ball.restart()

    #checking if the ball is passing the player side paddle, if yes up the score for pc
    elif ball.xcor() < -362:
        player_score.score_up()
        ball.restart()


screen.exitonclick()
