from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_COLOR = "white"
PADDLE_HEADING = 90
MOVE_STEP = 5


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.seth(PADDLE_HEADING)
        self.color(PADDLE_COLOR)
        self.penup()
        self.setpos(position)

    def up(self):
        self.fd(MOVE_STEP)

    def down(self):
        self.bk(MOVE_STEP)
