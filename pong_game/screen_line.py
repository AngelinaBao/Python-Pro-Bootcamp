from turtle import Turtle

LINE_WIDTH = 5
START_POSITION = (0, -300)
MOVE_STEP = 20
MOVE_COUNT = 15


class ScreenLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(width=LINE_WIDTH)
        self.hideturtle()
        self.penup()
        self.goto(START_POSITION)
        self.seth(90)
        self.speed(0)
        self.draw_dash_line()

    def draw_dash_line(self):
        for _ in range(MOVE_COUNT):
            self.penup()
            self.forward(MOVE_STEP)
            self.pendown()
            self.forward(MOVE_STEP)
