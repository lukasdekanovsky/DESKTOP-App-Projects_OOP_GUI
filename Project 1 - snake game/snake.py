from turtle import Turtle
import random


# ---- CONSTANTS ------------------------------
MOVE_DISTANCE = 20
COLOR = ["AntiqueWhite", "AntiqueWhite1", "AntiqueWhite2"]

class Snake:

    def __init__(self):
        self.start_position = [(0,0), (-20,0), (-40, 0)]
        self.segments = []                              # first empty
        self.create_snake()                             # filling with 3 segments
        self.snake_head = self.segments[0]              # evaluation of where head is located
        self.facing_direction = self.segments[0].heading() 
    
    #--------------------------------------------------------------------------------

    def create_snake(self):      
        """Creation of the initial 3 segment snake"""     
        for position in self.start_position:
            self.add_segment(position)
    
    def move(self):
        """Move with the snake segments via move distance constant"""
        # now we neer to range snake of the snake from the back
        for seg_num in range(len(self.segments)-1, 0, -1): # 2 -> 1 -> 0
            new_x = self.segments[seg_num - 1].xcor()      # before the last segment position
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)      # last segment will go to the position of the second last
        self.snake_head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color(random.choice(COLOR))
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        self.__init__()

    # onkey methods for setting the snake heading + avoiding moving up/down right/left forbidden moves
    # avoided moves aborded via self.facing_direction attribute
    def up(self):
        if self.facing_direction == 270:
            pass
        else:
            self.facing_direction = 90
            self.snake_head.setheading(90)

    def down(self):
        if self.facing_direction == 90:
            pass
        else:
            self.facing_direction = 270
            self.snake_head.setheading(270)

    def left(self):
        if self.facing_direction == 0:
            pass
        else:
            self.facing_direction = 180
            self.snake_head.setheading(180)

    def right(self):
        if self.facing_direction == 180:
            pass
        else:
            self.facing_direction = 0
            self.snake_head.setheading(0)


