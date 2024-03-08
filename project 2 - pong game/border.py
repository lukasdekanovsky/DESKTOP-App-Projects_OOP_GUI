from turtle import Turtle

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("azure4")
        self.penup()
        self.goto(-380, -280)
        self.pendown()
        self.width(5)
        self.move()
        self.hideturtle()
    
    def move(self):
        self.goto(-380, 280)
        self.goto(380, 280)
        self.goto(380, -280)
        self.goto(-380, -280)


