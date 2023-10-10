import turtle
import pandas as pd


state_data = pd.read_csv("./us-states-game/left_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

score = 0
is_game_on = True
guess_states = []

while is_game_on:
    answer_state = screen.textinput(
        title=f"{score}/{len(state_data.state)} States correct",
        prompt="what's another state's name?",
    ).title()

    if len(guess_states) == 50:
        is_game_on = False

    if answer_state == "Exit":
        new_state_data = state_data[~state_data["state"].isin(guess_states)]
        new_state_data.to_csv("./us-states-game/left_states.csv", index=False)
        break

    if answer_state in state_data["state"].to_list():
        if answer_state in guess_states:
            pass
        else:
            score += 1
            guess_states.append(answer_state)
            x = int(state_data[state_data["state"] == answer_state]["x"])
            y = int(state_data[state_data["state"] == answer_state]["y"])
            write_turtle = turtle.Turtle()  # create another turtle
            write_turtle.penup()
            write_turtle.hideturtle()
            write_turtle.color("black")
            write_turtle.goto(x, y)
            write_turtle.write(
                f"{answer_state}", False, align="left", font=("Arial", 10, "normal")
            )
