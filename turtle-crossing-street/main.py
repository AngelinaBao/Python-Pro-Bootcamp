import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()

    for car in cars.car_groups:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.reach_finish_line():
        player.reset_position()
        cars.speed_up()
        score.level_up()

screen.exitonclick()
