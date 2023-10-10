from turtle import Turtle

FONT = ("Arial", 16, "normal")
GAME_OVER_FONT = ("Arial", 20, "bold")
TEXT_POSITION = (-270, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(TEXT_POSITION)
        self.update_level()

    def update_level(self):
        self.write(f"level: {self.level}", False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"GAME OVER!", False, align="center", font=GAME_OVER_FONT)
