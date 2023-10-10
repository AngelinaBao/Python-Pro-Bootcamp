import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("classic")
tim.pensize(15)
tim.speed("fastest")

colors = ["#4169E1", "#87CEFA", "#EEE8AA", "#F4A460", "#DA70D6", "#F0E68C", "#FFC0CB"]
directions = [0, 90, 180, 270]

for _ in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)
    tim.forward(30)
    tim.setheading(random.choice(directions))


my_screen = t.Screen()
my_screen.exitonclick()
