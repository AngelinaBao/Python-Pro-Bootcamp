from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_QUANITY = 300
CAR_X_RANGE_L = -275
CAR_X_RANGE_R = 8000
CAR_Y_RANGE = 250


class CarManager:
    def __init__(self):
        self.car_groups = []
        self.init_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        position = (
            random.randint(CAR_X_RANGE_L, CAR_X_RANGE_R),
            random.randint(CAR_Y_RANGE * (-1), CAR_Y_RANGE),
        )
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.seth(180)
        new_car.penup()
        new_car.goto(position)
        self.car_groups.append(new_car)

    def init_car(self):
        for _ in range(CAR_QUANITY):
            self.create_car()

    def move(self):
        for car in self.car_groups:
            car.fd(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
