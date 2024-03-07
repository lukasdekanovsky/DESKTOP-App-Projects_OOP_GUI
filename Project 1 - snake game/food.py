from turtle import Turtle
import random

class Food(Turtle):   # Food class is inherited from parent class Turtle = it has all the methods and attributes

    def __init__(self):   # initialization of the individual food dot 
        super().__init__() 
        self.shape("circle") 
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  
        self.color("DarkSlateGrey")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def set_new_location(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)