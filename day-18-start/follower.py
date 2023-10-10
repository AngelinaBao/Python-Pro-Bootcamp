import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(73):
    tim.pencolor(color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)


screen = t.Screen()
screen.exitonclick()
