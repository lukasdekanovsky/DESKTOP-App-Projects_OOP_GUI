import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# ------------- SCREEN INIT -----------------
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# -------------- PLAYER INIT ---------------
player = Player()

screen.listen()
screen.onkey(player.up, "Up")

# ------------- PLAYER MANAGER -------------
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:   # on every refresh of the screen this will happend
    time.sleep(0.1)
    screen.update()
    score.update_score()

    # TODO 1) generate cars 
    cars.create_car()
    cars.move_cars()

    # TODO 2) limit the lenght of the list of created cars - code speed optimalization
    cars.reduce_car_list()

    # TODO 3) detect the turtle crashed the car
    y_cor_player = player.return_player_y_position()

    if cars.detect_collision(y_cor_player): # hit event trigered - game over
        game_is_on = False
        score.write_game_over()
        
    # TODO 4) detect next level 
    if player.ycor() >= 280:
        cars.next_level()
        player.move_to_start()
        score.clear()
        score.increase_level()
        score.update_score()
    
    # TODO 5) score 
      
    



screen.exitonclick()