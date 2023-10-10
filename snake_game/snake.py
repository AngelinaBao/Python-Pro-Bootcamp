from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_GAP = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.initial_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.is_collison = False

    def create_snake(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def initial_snake(self):
        for pos in STARTING_POSITION:
            self.create_snake(position=pos)

    def add_snake(self):
        self.create_snake(position=(self.tail.xcor(), self.tail.ycor()))

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    # detect collision
    def hit_the_wall(self):
        if (
            self.head.xcor() >= 285
            or self.head.ycor() >= 285
            or self.head.xcor() <= -285
            or self.head.ycor() <= -285
        ):
            self.is_collison = True
        return self.is_collison

    def hit_the_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 15:
                self.is_collison = True
        return self.is_collison
