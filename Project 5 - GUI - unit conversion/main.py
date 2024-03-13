from tkinter import *

def set_window(window):
    window.title("Miles to Km Converter")
    window.minsize(width=400, height=200)
    window.config(padx=50, pady=50)
   
def set_labels():
    main_label = Label(text="Type miles and hit calculate", font=("Arial", 10))
    main_label.grid(column=2, row=1)

    miles_label = Label(text="Miles")
    miles_label.grid(column=3, row=2)

    kilometer_label = Label(text="Km")
    kilometer_label.grid(column=3, row=3)

    equal_label = Label(text="is equal to")
    equal_label.grid(column=1, row=3)

def main_functionality():
    # ----- Main part of the program ------ -> input, output and action button
    miles_entry = Entry(width=15)
    miles_entry.grid(column=2, row=2)

    result_label = Label(text="0")
    result_label.grid(column=2, row=3)

    button = Button(text="Calculate", command= lambda: calculate(miles_entry, result_label))
    button.grid(column=2, row=4)

def calculate(miles_entry, result_label):
    miles_entry_input = float(miles_entry.get())   # input of miles
    kilometer_output = round((miles_entry_input * 1.60934), 2)
    result_label.config(text=kilometer_output)


def main():
    window = Tk()
    # ----- START ----------
    set_window(window)
    set_labels()

    main_functionality()

    # ----- END -------------
    window.mainloop()
    

if __name__ == "__main__":
    main()
