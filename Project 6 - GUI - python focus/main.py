import tkinter as tk
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
SHORT_BREAK_COLOR = "#891652"
LONG_BREAK_COLOR = "#240A34"
TIMER = "#8EACCD"
BACKGROUND = "#D2E0FB"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------------------------------------------------- #

def set_window(window, canvas, focus_image):
    window.title("Mind focus app")
    window.config(padx=20, pady=20, bg=BACKGROUND)
    
    canvas.create_image(100, 100, image = focus_image) # image center
    timer_text = canvas.create_text(100, 70, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
    canvas.grid(column=2, row=2)
    return timer_text

def set_main_label(text, color):
    main_label = tk.Label(text=text, font=(FONT_NAME, 35, "bold"), fg=color, bg=BACKGROUND)
    main_label.grid(column=2, row=1, pady= 20)
    return main_label

def update_checkmark(checkmark_label, mark):
    checkmark_label.config(text=mark)

def set_buttons(main_label, checkmark_label, timer_text, window, canvas):
    button_start = tk.Button(text="Start",font=(FONT_NAME, 10, "bold"), command= lambda: start_button_function(main_label, checkmark_label, timer_text, window, canvas), width=7, height=2)
    button_start.grid(column=1, row=3, padx=10)
    button_reset = tk.Button(text="Reset",font=(FONT_NAME, 10, "bold"), command= lambda: reset_button_function(main_label, checkmark_label, timer_text, window, canvas), width=7, height=2)
    button_reset.grid(column=3, row=3, padx=10)

def count_down(main_label, checkmark_label, timer_text, window, canvas, count):

    # formating algorithm from 110s -> to the 1 : 50
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, main_label, checkmark_label, timer_text, window, canvas, count-1)
    else:
        start_button_function(main_label, checkmark_label, timer_text, window, canvas)
        mark = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            mark += "✔"
        update_checkmark(checkmark_label, mark)

def start_button_function(main_label, checkmark_label, timer_text, window, canvas):
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 8 == 0:
        count_down(main_label, checkmark_label, timer_text, window, canvas, long_break_sec)
        main_label.config(text="Break!", fg=LONG_BREAK_COLOR)
    elif reps % 2 == 0:
        count_down(main_label, checkmark_label, timer_text, window, canvas, short_break_sec)
        main_label.config(text="Break!", fg=SHORT_BREAK_COLOR)
    else:
        count_down(main_label, checkmark_label, timer_text, window, canvas, work_sec)
        main_label.config(text="Code!", fg=TIMER)
        

def reset_button_function(main_label, checkmark_label, timer_text, window, canvas):
    window.after_cancel(timer)                 # stop time
    main_label.config(text="Timer", fg=TIMER)  # reset main_label
    canvas.itemconfig(timer_text, text = "00:00")
    update_checkmark(checkmark_label, mark="")
    global reps
    reps = 0

def main():
    # object init
    window = tk.Tk()
    canvas = tk.Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness = 0)
    focus_image = tk.PhotoImage(file="python.png")  

    
    checkmark_label = tk.Label(text="", fg=TIMER, bg=BACKGROUND, font=(FONT_NAME, 25, "bold"))
    checkmark_label.grid(column=2, row=4)


    timer_text = set_window(window, canvas, focus_image)
    main_label = set_main_label(text="Timer", color=TIMER)
    set_buttons(main_label, checkmark_label, timer_text, window, canvas) 
    
    window.mainloop()

if __name__ == "__main__":
    main()