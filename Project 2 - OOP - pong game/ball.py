from turtle import Turtle

#--------- CONSTANTS --------
MOVE_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("azure")
        self.setheading(45)

    def move(self):
        self.speed("normal")
        self.set_actual_heading()
        self.forward(MOVE_SPEED)

    def return_y_middle_point(self):
        return (self.ycor())

    def return_x_middle_point(self):
        return (self.xcor())
        
    def set_actual_heading(self):
        """Function sets adequate heading of the ball depending on bounce_type"""
        if self.evaluate_bounce_type() == True:          # paddle bounce
            self.paddle_bounce()
        elif self.evaluate_bounce_type() == False:       # top down bounce
            self.horizontal_bounce()
        else:
            pass 

    def evaluate_bounce_type(self):
        """Returns True if Left/Right hitted || returns False if Top/Bottom hitted"""
        if self.xcor() > 330 or self.xcor() < -330:# and collision???:   # Fail game
            return True  
        elif self.ycor() > 280 or self.ycor() < -280:
            return False
        else:
            pass  # reset ball 


    def horizontal_bounce(self):
        if self.heading() in range(0,90): # in case ball is flying with heading 45 -> bouncing back with 315 
            self.setheading(315)
        elif self.heading() in range(90, 180):
            self.setheading(225)
        elif self.heading() in range(180, 270):
            self.setheading(135)
        elif self.heading() in range(270, 360):
            self.setheading(45)
    
    def paddle_bounce(self):
        if self.heading() in range(0,90): # in case ball is flying with heading 45 -> bouncing back with 315 
            self.setheading(135)
        elif self.heading() in range(90, 180):
            self.setheading(45)
        elif self.heading() in range(180, 270):
            self.setheading(315)
        elif self.heading() in range(270, 360):
            self.setheading(225)