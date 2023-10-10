from turtle import Turtle

INIT_POSITION = (0, 0)
MOVE_STEP = 5
MOVE_SPEED = 0.1
MOVE_RATE = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.setpos(INIT_POSITION)
        self.penup()
        self.x_move = MOVE_STEP
        self.y_move = MOVE_STEP
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # if hit the wall then bounce away

    def bounce_x(self):
        self.x_move *= -1  # if hit the paddles then bounce to the opposite side
        self.move_speed *= MOVE_RATE  # if hit the paddles then speed slow down

    def init_ball(self):
        self.goto(INIT_POSITION)
        self.move_speed = MOVE_SPEED
        self.bounce_x()
