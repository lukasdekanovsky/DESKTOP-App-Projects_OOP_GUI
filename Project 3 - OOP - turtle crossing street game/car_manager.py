from turtle import Turtle
import random

COLORS = ["AntiqueWhite2", "SteelBlue3", "DarkSeaGreen2", "azure3", "CadetBlue1", "DarkOliveGreen2", "DarkSlateGrey"]
INITIAL_SPEED = 2
INCREASE_SPEED_INCREMENT = 1

class CarManager:

    def __init__(self):
        self.all_cars = [] 
        self.speed = INITIAL_SPEED
        self.frequency = [1, 20]
        
    def create_car(self):
        random_chance = random.randint(self.frequency[0], self.frequency[1])            # slow down the car creation
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-250, 250, 50)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for each_car in self.all_cars:
            each_car.backward(self.speed)


    def reduce_car_list(self):
        for car in self.all_cars:
            if car.xcor() < -340:
                self.all_cars.remove(car)

    def detect_collision(self, y_cor_player): 
        for car in self.all_cars:
            if car.xcor() in range(-10, 10) and y_cor_player in range(int(car.ycor())-20, int(car.ycor())+20):
                return True
            
    def next_level(self):
        """Next level function increses frequency of cars created + ncreases their speed"""
        self.speed += INCREASE_SPEED_INCREMENT
        if self.frequency[1] >= 1:
            self.frequency[1] -= 1
        
        
            


            
        