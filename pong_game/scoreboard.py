from turtle import Turtle

SCORE_ALIGN = "center"
FONT = ("Courier", 60, "bold")
GAME_OVER_FONT = ("Courier", 15, "bold")
LEFT_SCORE_POSITION = (-150, 200)
RIGHT_SCORE_POSITION = (150, 200)
GAME_OVER_TEXT_POS = (-25, 0)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_score()
        self.is_game_on = True
        self.winner_player = str()

    def update_score(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(
            f"{self.score_l}",
            False,
            align=SCORE_ALIGN,
            font=FONT,
        )
        self.goto(RIGHT_SCORE_POSITION)
        self.write(
            f"{self.score_r}",
            False,
            align=SCORE_ALIGN,
            font=FONT,
        )

    def l_point(self):
        self.score_l += 1
        self.update_score()

    def r_point(self):
        self.score_r += 1
        self.update_score()

    def winner(self):
        if self.score_l > self.score_r:
            return "left player"
        elif self.score_l < self.score_r:
            return "right player"
        else:
            return "Both two palyers"

    def game_over(self):
        self.is_game_on = False
        self.winner_player = self.winner()
        self.goto(GAME_OVER_TEXT_POS)
        self.write(
            f"Game OVER, Winner is {self.winner_player}.",
            False,
            align=SCORE_ALIGN,
            font=GAME_OVER_FONT,
        )
