from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from screen_line import ScreenLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong Game!")
screen.tracer(0)

paddle_l = Paddle(position=(-350, 0))
paddle_r = Paddle(position=(350, 0))
ball = Ball()
score = ScoreBoard()
dash_line = ScreenLine()

screen.listen()
# onkeypress can keep pressing a button and paddle keep going, but onkey is on click and one step movement
screen.onkeypress(paddle_l.up, "Up")
screen.onkeypress(paddle_l.down, "Down")
screen.onkeypress(paddle_r.up, "w")
screen.onkeypress(paddle_r.down, "s")
screen.onkey(score.game_over, "q")

while score.is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320 and ball.xcor() < 350) or (
        ball.distance(paddle_l) < 50 and ball.xcor() < -320 and ball.xcor() > -350
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.init_ball()
        score.l_point()

    if ball.xcor() < -380:
        ball.init_ball()
        score.r_point()

screen.exitonclick()
