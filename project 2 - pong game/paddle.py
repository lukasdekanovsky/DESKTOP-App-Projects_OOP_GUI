from turtle import Turtle

# ------- CONSTANTS -------------
MOVE_DISTANCE = 50
# -------------------------------

class Paddle:

    def __init__(self, start_positions):
        self.start_positions = start_positions
        self.segments = []
        self.create_paddle()

    def return_y_middle_point(self):
        return (self.segments[2].ycor())   # -> return int of the midle position of the paddle

    def create_paddle(self):
        for position in self.start_positions:
            new_paddle_segment = Turtle(shape="square")
            new_paddle_segment.color("azure")
            new_paddle_segment.penup()
            new_paddle_segment.goto(position)
            self.segments.append(new_paddle_segment)

    def up(self):
        for paddle_segment in self.segments[::-1]:
            if self.segments[0].ycor() < 210:
                new_y = paddle_segment.ycor() + MOVE_DISTANCE
                paddle_segment.goto(350, new_y)

    def down(self):
         for paddle_segment in self.segments:
            if self.segments[-1].ycor() > -210:
                new_y = paddle_segment.ycor() - MOVE_DISTANCE
                paddle_segment.goto(350, new_y)



class SecondPaddle(Paddle):

    def __init__(self, start_positions):
        super().__init__(start_positions)

    def up(self):
        for paddle_segment in self.segments[::-1]:
            if self.segments[0].ycor() < 210:
                new_y = paddle_segment.ycor() + MOVE_DISTANCE
                paddle_segment.goto(-350, new_y)

    def down(self):
         for paddle_segment in self.segments:
            if self.segments[-1].ycor() > -210:
                new_y = paddle_segment.ycor() - MOVE_DISTANCE
                paddle_segment.goto(-350, new_y)
    
