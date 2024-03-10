from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        

    def up(self):
        if self.ycor() >= FINISH_LINE_Y:
            return
        else:
            self.forward(MOVE_DISTANCE)

    def return_player_y_position(self):
        return self.ycor()
    
    def move_to_start(self):
        self.goto(STARTING_POSITION)
