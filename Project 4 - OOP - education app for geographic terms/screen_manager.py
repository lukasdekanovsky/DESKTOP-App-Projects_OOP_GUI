from turtle import Turtle

class ScreenManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def draw_state(self, position_x, position_y, state):
        self.goto(float(position_x), float(position_y))
        self.color("black")
        self.write(state, align="center", font = ("Courier", 8, "normal"))

    def draw_game_title(self):
        self.goto(0, 250)
        self.color("grey")
        self.write("Do you know all states in the U.S.? ", align="center", font = ("Courier", 12, "normal"))
    