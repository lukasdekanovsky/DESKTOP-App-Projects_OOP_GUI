from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.color("black")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
    
    def increase_level(self):
        self.level_number += 1

    def update_score(self):
        self.write(f"Level: {self.level_number}", align = "center", font = ("Courier", 18, "normal"))

    def write_game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align = "center", font = ("Courier", 24, "normal"))

