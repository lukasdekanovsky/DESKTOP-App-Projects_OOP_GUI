from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_a = 0
        self.score_b = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score A: {self.score_a}            score B: {self.score_b}", align = ALIGNMENT, font=FONT)

    def increase_score(self, winner):
        if winner == "player_a":
            self.score_a += 1
        elif winner == "player_b":
            self.score_b += 1

        self.clear()
        self.update_scoreboard()