import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from password_manager import PasswordManager
from file_manager import FileManager

# ---------------- CONSTANTS --------------- #
WINDOW_BACKGROUND = "#9BB0C1"
BUTTON_BACKGROUND = "#F5E8DD"
FONT_NAME = "Courier"
# ------------------------------------------ #

def open_file(file_manager):
    file_manager.open_file_dialog()


def generate_password_action(password_manager, password_text):
    if password_text.get() != "":
        messagebox.showerror(title="Error", message="Clear the password field before generating new password")
        want_clear =messagebox.askokcancel(title="Clear the field", message="Do you want to clear the password field?")
        if want_clear:
            password_text.delete(0, 50)
            return
        else:
            return
    
    generated_pasword = password_manager.generate_random_password()
    password_text.insert(0, generated_pasword)

    new_generation = messagebox.askokcancel(title="Password generated", message="Do you want to generate new password?")
    if new_generation:
        password_text.delete(0, 50)
    

def add_function(file_manager, password_manager, website_text, username_text, password_text, path):
    website = website_text.get()
    username = username_text.get() 
    password = password_text.get()  
    
    if file_manager.file_path == "":
        messagebox.showerror(title="Error", message="You did not selected file for your password management.\nPlease select the file in top right corner.")
        return
    
    if website_text.get() == "" or username_text.get() == "" or password_text.get() == "":
        messagebox.showinfo(title="Failed", message="Please don´t leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        password_manager.save_new_password(website, username, password, path)
        website_text.delete(0, 50)
        username_text.delete(0, 50)
        password_text.delete(0, 50)


def main():
    # ------------------------- WINDOW , CANVAS init ------------------------ #
    window = tk.Tk()
    canvas = tk.Canvas(width=280, height=320, bg=WINDOW_BACKGROUND, highlightthickness = 0)
    image = tk.PhotoImage(file="authentication.png")
    
    window.config(padx = 20, pady=20, bg=WINDOW_BACKGROUND)
    window.title("Password Manager")
    canvas.create_image(140, 130, image=image)
    canvas.create_text(140, 290, text="My password manager", fill="black", font=(FONT_NAME, 16, "bold"))
    canvas.grid(column=1, row=0)

    # -------------------------- LABELS -------------------------------------- #
    website_label = tk.Label(text="Website:", bg=WINDOW_BACKGROUND, pady=1)
    emai_username_label = tk.Label(text="Email/Username:", bg=WINDOW_BACKGROUND, pady=1)
    password_label = tk.Label(text="Password:", bg=WINDOW_BACKGROUND, pady=1)
    website_label.grid(column=0, row=1, sticky="ne", pady=1)
    emai_username_label.grid(column=0, row=2, sticky="ne", pady=1)
    password_label.grid(column=0, row=3, sticky="ne", pady=1)

    # -------------------------- TEXT ---------------------------------------- #
    website_text = tk.Entry(width=49)
    website_text.focus()
    username_text = tk.Entry(width=49)
    username_text.insert(0, "@gmail.com")
    password_text = tk.Entry(width=27)
    website_text.grid(column=1, row=1, columnspan=2, sticky="nw")
    username_text.grid(column=1, row=2, columnspan=2, sticky="nw")
    password_text.grid(column=1, row=3,sticky="nw")

    # -------------------------- MANAGERS ------------------------------------- #
    password_manager = PasswordManager(website_text, username_text, password_text)
    file_manager = FileManager()


    # -------------------------- BUTTON ---------------------------------------- #
    open_button = tk.Button(text="Select file", height=2, bg=BUTTON_BACKGROUND, command=lambda: open_file(file_manager))
    open_button.grid(column=3, row=0, sticky="nw")  
    generate_password_button = tk.Button(text="Generate Password", width= 15, height= 1, bg=BUTTON_BACKGROUND, command=lambda: generate_password_action(password_manager, password_text))
    add_button = tk.Button(text="Add", width= 22, height= 1, bg=BUTTON_BACKGROUND, command=lambda: add_function(file_manager, password_manager, website_text, username_text, password_text, file_manager.file_path))
    generate_password_button.grid(column=1, row=3, sticky="ne", pady=1)
    add_button.grid(column=1, row=4, columnspan=2, pady=1, sticky="sw")
    

    window.mainloop()

if __name__ == "__main__":
    main()