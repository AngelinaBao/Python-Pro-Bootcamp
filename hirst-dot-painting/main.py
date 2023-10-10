import turtle as t
import random

color_list = [
    (223, 236, 228),
    (236, 230, 216),
    (140, 176, 207),
    (26, 107, 159),
    (237, 225, 235),
    (209, 161, 111),
    (144, 29, 63),
    (230, 212, 93),
    (4, 163, 197),
    (218, 60, 84),
    (229, 79, 43),
    (195, 130, 169),
    (54, 168, 114),
    (28, 61, 116),
    (172, 53, 95),
    (108, 182, 90),
    (110, 99, 87),
    (193, 187, 46),
    (240, 204, 2),
    (1, 102, 119),
    (50, 150, 109),
    (172, 212, 172),
    (118, 36, 34),
    (221, 173, 188),
    (227, 174, 166),
    (153, 205, 220),
    (184, 185, 210),
]

hirst = t.Turtle()
t.colormode(255)
hirst.speed(0)

# change starting position
hirst.hideturtle()  # hide drawing arrow
hirst.penup()  # hide drawing lines
hirst.goto(-200, -200)


def hirst_dot_painting(width=20, height=50, steps=15):
    """
    plot hirst fot painting, wdith is dot quantity on x-axis,
    height is dot quantity on y-axis, steps is dot size and space between dots.
    """
    for _ in range(height):
        for _ in range(width):
            hirst.dot(steps, random.choice(color_list))
            hirst.forward(steps * 2)
        hirst.backward(steps * 2 * width)

        hirst.left(90)
        hirst.forward(steps * 2)
        hirst.right(90)


hirst_dot_painting(width=10, height=10)

screen = t.Screen()
screen.exitonclick()
