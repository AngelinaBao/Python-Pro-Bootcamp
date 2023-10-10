from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="user bet", prompt="Which turtle will win the race? choose a color: "
)
colors = ["yellow", "orange", "red", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# y = -150
# for i, color in enumerate(colors):
#     exec(f"new_turtle_{i} = Turtle(shape='turtle')")
#     exec(f"new_turtle_{i}.color(f'{color}')")
#     exec(f"new_turtle_{i}.penup()")
#     exec(f"new_turtle_{i}.goto(x=-230, y=y)")
#     y += 60

if user_bet:
    is_race_on = True

for tutle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tutle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[tutle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! {winner_color} is winning.")
            else:
                print(f"You've lost! {winner_color} is winning")

        random_step = random.randint(0, 10)
        turtle.forward(random_step)


screen.exitonclick()
