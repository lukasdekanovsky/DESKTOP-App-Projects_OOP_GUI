from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

def game():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game v_1.0")

    screen.tracer(0) 


    snake = Snake()                     
    food = Food()
    score = ScoreBoard()

    # ---------------- LOAD SYSTEM --------------------------
    with open("highest_score.txt", mode="r") as load_info:
        score_to_load = int(load_info.read())
    
    print(f"Highest score to load: {score_to_load}")
    score.high_score = score_to_load
    score.update_scoreboard()
    # ---------------- LOAD SYSTEM --------------------------

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_on = True
    while game_on:
        screen.update()         
        time.sleep(0.1)
        snake.move()           

        # TODO 1) logic of food administration - snake grow
        if snake.snake_head.distance(food) < 15:
            food.set_new_location() 
            score.increase_score()
            snake.extend_snake()

        # TODO 2) logic of wall hit and score administration
        if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
            score.reset()
            play_again = screen.textinput(title="Game Over", prompt="Do you want to play again. Type 'y' or 'n': ").upper()
            if play_again == "Y":
                screen.listen()
                snake.reset()
            else:
                game_on = False
                save_or_reset = screen.textinput(title="Save/Load", prompt="Do you want to SAVE or RESET high score. Type 's' or 'r': ").upper()
                if save_or_reset == "S":
                    # ---------------- SAVE SYSTEM --------------------------
                    with open("highest_score.txt", mode="w") as save_info:
                        save_info.write(str(score.high_score))
                        print(f"Highest score to save: {score.high_score}")
                    # ---------------- SAVE SYSTEM --------------------------
                else:
                    # ---------------- RESET SYSTEM --------------------------
                    with open("highest_score.txt", mode="w") as save_info:
                        save_info.write("0")
                    # ---------------- RESET SYSTEM --------------------------

        # TODO 3) logic of tail hit and score administration
        for segment in snake.segments:
            if segment == snake.snake_head:
                pass
            elif snake.snake_head.distance(segment) < 5:
                score.reset()
                play_again = screen.textinput(title="Game Over", prompt="Do you want to play again. Type 'y' or 'n': ").upper()
                if play_again == "Y":
                    screen.listen()
                    snake.reset()
                else:
                    game_on = False
            
def main():
    game()
    screen.exitonclick()


if __name__ == "__main__":
    main()