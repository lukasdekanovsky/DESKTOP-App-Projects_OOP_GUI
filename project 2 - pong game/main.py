from turtle import Screen
from paddle import Paddle, SecondPaddle
from ball import Ball
from border import Border
from scoreboard import ScoreBoard
import time

# ---------------- CONSTANTS ------
START_POSITIONS_A = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]
START_POSITIONS_B = [(-350, -40), (-350, -20), (-350, 0), (-350, 20), (-350, 40)]
#----------------------------------

def setup_screen(screen):
    """Setup initial scree with black bg, 800x600 and corresponding title"""
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG game v_1.1")
    screen.tracer(0)

def game(screen, ball, paddle_a, paddle_b, score):
    """Main game logic loop"""
    game_on = True
    while game_on:
        screen.update()         
        time.sleep(0.01)
        # ---------------------- MAIN GAME LOGIC ----------------------------------- 
        # TODO 1: Ball move function 
        ball.move() # -> moving with initial angle of 45

        # TODO 2: Ball collision with paddles
        paddle_a_middle_coordinates = paddle_a.return_y_middle_point()
        paddle_b_middle_coordinates = paddle_b.return_y_middle_point()
        ball_x_coordinates = int(ball.return_x_middle_point())
        ball_y_coordinates = int(ball.return_y_middle_point())

        # TODO 3: Score
        if ball_x_coordinates < 330 and ball_x_coordinates > - 330:
            pass  # ball in between
        elif ball_x_coordinates > 330 and ball_y_coordinates not in range(paddle_a_middle_coordinates - 60, paddle_a_middle_coordinates + 60):
            score.increase_score("player_a")
        elif ball_x_coordinates < 330 and ball_y_coordinates not in range(paddle_b_middle_coordinates - 60, paddle_b_middle_coordinates + 60):
            score.increase_score("player_b")
        
    score.update_scoreboard()
        

def main():
    # --------------------------- SCREEN INIT ---------------------------------------
    screen = Screen()
    setup_screen(screen)
    screen.listen()

    # --------------------------- PADDLE INIT ---------------------------------------
    paddle_a = Paddle(START_POSITIONS_A)
    paddle_b = SecondPaddle(START_POSITIONS_B)
    screen.onkey(paddle_a.up, "Up")
    screen.onkey(paddle_a.down, "Down")
    screen.onkey(paddle_b.up, "w")
    screen.onkey(paddle_b.down, "s")
    
    # --------------------------- BALL INIT -----------------------------------------------
    ball = Ball()
    border_line = Border()
    
    # --------------------------- SCORE INIT ----------------------------------------------
    score = ScoreBoard()
    
    # ------------------------- MAIN GAME LOOP -------------
    game(screen, ball, paddle_a, paddle_b, score)
    
    

    # Finish screen
    screen.exitonclick()

if __name__ == "__main__":
    main()