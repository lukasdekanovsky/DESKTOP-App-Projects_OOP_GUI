import turtle
from turtle import Screen
from state_manager import StateManager
from screen_manager import ScreenManager

def get_mouse_click_coor(x, y):
    print(x, y)

def main():
    screen = Screen()
    screen.title("U.S. sates QUIZ")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    # turtle.onscreenclick(get_mouse_click_coor) -> for setting up new images and Quizes

    # --------------------------- Objects init ------------------------------
    state_manager = StateManager()
    screen_manager = ScreenManager()

    screen_manager.draw_game_title()

    app_on = True
    while app_on:
        # ------------------------- Player answers ---------------------------
        if state_manager.score > 0:
            answer = screen.textinput(title=f"{state_manager.score}/50 States Correct", prompt="Type another state name:\nType \"end\" back to main menu").title()
        else:
            answer = screen.textinput(title="Guess the State", prompt="What´s some state name?:\nType \"end\" back to main menu").title()
        
        # --------------------------- Main menu ------------------------------------
        if answer == "End":
            menu = screen.textinput(title="Menu", prompt="Continue/Exit (c/e):\nExit will process .csv file with all states to be learned.").upper()
            if menu == "C":
                pass
            else:
                app_on = False
                state_manager.create_learning_csv()
                return
        # -------------------- Check if answer is correct --------------------------
        try:
            position_x, position_y = state_manager.check_correct_answer(answer)
            screen_manager.draw_state(position_x, position_y, answer)
        except:
            pass

    turtle.mainloop()

if __name__ == "__main__":
    main()