from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Welcome to Snake Game")

snake = Snake()
food = Food()
user_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_go_on = True
while game_go_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect the food
    if snake.head.distance(food) < 15:
        food.fresh()
        user_score.clear()
        user_score.increase_score()
        snake.add_snake()

    if snake.hit_the_wall() or snake.hit_the_tail():
        user_score.game_over()
        game_go_on = False


screen.exitonclick()
