from turtle import Turtle

SCORE_POSITION = (0, 280)
SCORE_ALIGN = "center"
FONT = ("Arial", 11, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(
            f"score: {self.score}",
            False,
            align=SCORE_ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "Game OVER",
            False,
            align=SCORE_ALIGN,
            font=FONT,
        )
