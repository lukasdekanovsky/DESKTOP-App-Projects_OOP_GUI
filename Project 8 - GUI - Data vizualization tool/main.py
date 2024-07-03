# "C:\LukasADVACAM\Data" is the path to the folder where the data is stored

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage, Label
import os


from data_manager import DataManager
from processing_manager import ProcessingManager

# ----------------------------------------------#
# ----------------- CONSTANTS--------------------#
# ----------------------------------------------#
ROOT_BACKGROUND = "white"
LOGO_FRAME_BACKGROUND = "#20B2AA"
PROCESSING_FRAME_BACKGROUND = "#E0EEEE"
DATA_FRAME_BACKGROUND = "#E0EEEE"
IMAGE_FRAME_BACKGROUND = "#E0EEEE"
EXPORT_FRAME_BACKGROUND = "#E0EEEE"
PROCESS_BUTTON_COLOR = "#FFB6C1"
PROCESS_BUTTON_COLOR = "#FFB6C1"
REINIT_BUTTON_COLOR = "#FFEC8B"
IMAGE_BUTTON_COLOR = "#7FFFD4"
ARROW_BACKGROUND = "white"

LOGO_FONT = ('Helvetica', 20, "bold")
FRAME_LABELS = ('Helvetica', 10, "bold")
AUTHOR_LABEL = ('Helvetica', 8, "italic")

FRAME_SUBLABEL_1 = ('Helvetica', 10)
BUTTON_LABEL_A = ('Helvetica', 8)
BUTTON_LABEL_B = ('Helvetica', 9)
BUTTON_LABEL_B = ('Helvetica', 9)
BUTTON_LABEL_C = ('Helvetica', 10)
ARROW_FONT = ('Helvetica', 10, "bold")

# ----------------------------------------------#
# ----------------- FUNCTIONS ------------------#
# ----------------------------------------------#
def reinitialize(root):
    root.destroy()
    main()

# ----------------------------------------------#
# ----------------- UI-SETUP--------------------#
# ----------------------------------------------#

def main():

    root = Tk()                         # create root window
    root.title("FLAT_XRF")              # set title of the window
    root.maxsize(850, 850)              # set maximum size of the window
    root.config(bg=ROOT_BACKGROUND)     # set background color of the window


    # ------------------------#
    # ----- FRAMES SETUP -----#
    # ------------------------#
    # data processing selection frame with bools for processing steps
    processing_frame = Frame(root, width=300, height=100, bg=PROCESSING_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)
    processing_frame.grid(row=1, column=0, padx=10, pady=5)

    # data frame for data load, delete and run the visualization
    data_frame = Frame(root, width=300, height=560, bg=DATA_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)
    data_frame.grid(row=2, column=0, rowspan=3, padx=10, pady=5)

    # logo frame for the SW name and image
    logo_frame = Frame(root, width=500, height=100, bg=LOGO_FRAME_BACKGROUND)
    logo_frame.grid(row=1, column=1, padx=10, pady=5)

    # image frame - main visualization window
    image_frame = Frame(root, width=500, height=500, bg=IMAGE_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=2)
    image_frame.grid(row=2, column=1, padx=10, pady=5)

    # export fram - options for image save or other postprocessing?
    export_frame = Frame(root, width=500, height=50, bg=EXPORT_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)
    export_frame.grid(row=3, column=1, padx=10, pady=5)

    Label(logo_frame, text="FLAT_XRF", font=LOGO_FONT, bg=LOGO_FRAME_BACKGROUND).place(relx=0.15, rely=0.20, anchor=CENTER)
    Label(logo_frame, text="lukasdekanovsky@gmail.com", font=AUTHOR_LABEL, bg=LOGO_FRAME_BACKGROUND).place(relx=0.84, rely=0.85, anchor=CENTER)
    Label(processing_frame, text="Processing selection", font=FRAME_LABELS, bg=PROCESSING_FRAME_BACKGROUND).place(relx=0.5, rely=0.13, anchor=CENTER)
    Label(data_frame, text="Data", font=FRAME_LABELS, bg=DATA_FRAME_BACKGROUND).place(relx=0.5, rely=0.02, anchor=CENTER)
    Label(image_frame, text="Image frame", font=FRAME_LABELS, bg=IMAGE_FRAME_BACKGROUND).place(relx=0.5, rely=0.022, anchor=CENTER)
    Label(export_frame, text="Export", font=FRAME_LABELS, bg=EXPORT_FRAME_BACKGROUND).place(relx=0.05, rely=0.5, anchor=CENTER)


    # ----------------------------#
    # ----- PROCESSING FRAME -----#
    # ----------------------------#
    selection_2D_image = BooleanVar()
    selection_2D_CT_scan = BooleanVar()
    selection_FF = BooleanVar()
    selection_4 = BooleanVar()

    Checkbutton(processing_frame, text="2D image", variable=selection_2D_image, onvalue=True, offvalue=False).place(relx=0.10, rely=0.4, anchor=W)
    Checkbutton(processing_frame, text="2D CT scan - gif", variable=selection_2D_CT_scan, onvalue=True, offvalue=False).place(relx=0.10, rely=0.8, anchor=W)
    Checkbutton(processing_frame, text="Flat field", variable=selection_FF, onvalue=True, offvalue=False).place(relx=0.6, rely=0.4, anchor=W)
    Checkbutton(processing_frame, text="Option 4", variable=selection_4, onvalue=True, offvalue=False).place(relx=0.6, rely=0.8, anchor=W)
    # ---> selection_2D_image.get()  ZISKAVAME TRUE/FALSE HODNOTU Z CHEKCBOXU


    # class instances as managers
    data_manager = DataManager(root)


    # ----------------------------#
    # -------- DATA FRAME --------#
    # ----------------------------#
    
    #  -----------------------------LOADED DATA_a listbox------------------------------------------------ #
    #  -------------------------------------------------------------------------------------------------- #
    # DATA FOLDERS
    loaded_data_a_folder = "./data_a"
    loaded_data_a = os.listdir(loaded_data_a_folder)
    # LISTBOX
    Label(data_frame, text="Loaded data A", font=FRAME_SUBLABEL_1, bg=DATA_FRAME_BACKGROUND).place(relx=0.16, rely=0.08, anchor=CENTER)
    loaded_data_a_scrollbar = tk.Scrollbar(data_frame)
    loaded_data_a_scrollbar.place(relx=0.46, rely=0.25, anchor=CENTER, relheight=0.3)
    loaded_data_a_listbox = tk.Listbox(data_frame, yscrollcommand=loaded_data_a_scrollbar.set, width=30, height=10)
    loaded_data_a_listbox.place(relx=0.215, rely=0.25, width=120, anchor=CENTER)
    # SHOW ALL FILES in Listbox
    for data in loaded_data_a:
        loaded_data_a_listbox.insert(tk.END, data)
    # BUTTONS
    Button(data_frame, text="Load data", font=BUTTON_LABEL_A, command = lambda: data_manager.load_data_a(loaded_data_a_listbox)).place(relx=0.11, rely=0.43, anchor=CENTER)
    Button(data_frame, text="Delete data", font=BUTTON_LABEL_A, command=lambda: data_manager.delete_data_a(loaded_data_a_listbox)).place(relx=0.33, rely=0.43, anchor=CENTER)
   #  -------------------------------------------------------------------------------------------------- #
   #  -------------------------------------------------------------------------------------------------- #


   #  -----------------------------LOADED DATA_b listbox------------------------------------------------ #
   #  -------------------------------------------------------------------------------------------------- #
   # DATA FOLDERS
    loaded_data_b_folder = "./data_b"
    loaded_data_b = os.listdir(loaded_data_b_folder)
    # LISTBOX
    Label(data_frame, text="Loaded data B", font=FRAME_SUBLABEL_1, bg=DATA_FRAME_BACKGROUND).place(relx=0.65, rely=0.08, anchor=CENTER)
    loaded_data_b_scrollbar = tk.Scrollbar(data_frame)
    loaded_data_b_scrollbar.place(relx=0.95, rely=0.25, anchor=CENTER, relheight=0.3)
    loaded_data_b_listbox = tk.Listbox(data_frame, yscrollcommand=loaded_data_b_scrollbar.set, width=30, height=10)
    loaded_data_b_listbox.place(relx=0.705, rely=0.25, width=120, anchor=CENTER)
    # SHOW ALL FILES in Listbox
    for data in loaded_data_b:
        loaded_data_b_listbox.insert(tk.END, data)
    # BUTTONS
    Button(data_frame, text="Load data", font=BUTTON_LABEL_A, command = lambda: data_manager.load_data_b(loaded_data_b_listbox)).place(relx=0.60, rely=0.43, anchor=CENTER)
    Button(data_frame, text="Delete data", font=BUTTON_LABEL_A, command=lambda: data_manager.delete_data_b(loaded_data_b_listbox)).place(relx=0.82, rely=0.43, anchor=CENTER)
    #  -------------------------------------------------------------------------------------------------- #
    #  -------------------------------------------------------------------------------------------------- #


    #  -----------------------------PROCESSED DATA listbox----------------------------------------------- #
    #  -------------------------------------------------------------------------------------------------- #
    # DATA FOLDERS
    results_folder = "./results"
    results_data = os.listdir(results_folder)

    Label(data_frame, text="Processed data", font=FRAME_SUBLABEL_1, bg=DATA_FRAME_BACKGROUND).place(relx=0.19, rely=0.57, anchor=CENTER)
    processed_data_scrollbar = tk.Scrollbar(data_frame)
    processed_data_scrollbar.place(relx=0.9, rely=0.75, anchor=CENTER, relheight=0.3)
    processed_data_listbox = tk.Listbox(data_frame, yscrollcommand=processed_data_scrollbar.set, width=30, height=10)
    processed_data_listbox.bind("<Double-Button-1>", lambda x: processing_manager.open_file())
    processed_data_listbox.place(relx=0.42, rely=0.75, width=230, anchor=CENTER)
    # SHOW ALL FILES in Listbox
    for data in results_data:
        processed_data_listbox.insert(tk.END, data)
    # BUTTONS
    Button(data_frame, text="Clear results", font=BUTTON_LABEL_A, command=lambda: data_manager.delete_data_results(processed_data_listbox)).place(relx=0.15, rely=0.94, anchor=CENTER)
    #  -------------------------------------------------------------------------------------------------- #
    #  -------------------------------------------------------------------------------------------------- #

    processing_manager = ProcessingManager(root, loaded_data_a_listbox, loaded_data_b_listbox, processed_data_listbox)

    # PROCESS BUTTON
    Button(data_frame, width=15, text="Process", font=BUTTON_LABEL_B, bg=PROCESS_BUTTON_COLOR, command=lambda: processing_manager.process_data(selection_2D_image, selection_2D_CT_scan, selection_FF, selection_4)).place(relx=0.66, rely=0.485, anchor=CENTER)
    Button(data_frame, width=15, text="Reinitialize window", font=BUTTON_LABEL_B, bg=REINIT_BUTTON_COLOR, command=lambda: reinitialize(root)).place(relx=0.26, rely=0.485, anchor=CENTER)
    Button(data_frame, width=15, text="Open in frame", font=BUTTON_LABEL_C, bg=IMAGE_BUTTON_COLOR, command=lambda: data_manager.image_to_frame(image_frame, processed_data_listbox)).place(relx=0.58, rely=0.94, anchor=CENTER)


    # ----------------------------#
    # -------- IMAGE FRAME -------#
    # ----------------------------#
    #if processed_data_listbox.size() > 0:
    left_arrow_button = Button(image_frame, text="<", font=ARROW_FONT, bg=ARROW_BACKGROUND)
    left_arrow_button.bind("<Button-1>", lambda x: data_manager.change_image('left', processed_data_listbox, image_frame))
    left_arrow_button.place(relx=0.02, rely=0.5, anchor=CENTER)
    right_arrow_button = Button(image_frame, text=">", font=ARROW_FONT, bg=ARROW_BACKGROUND)
    right_arrow_button.bind("<Button-1>", lambda x: data_manager.change_image('right', processed_data_listbox, image_frame))
    right_arrow_button.place(relx=0.98, rely=0.5, anchor=CENTER)

    


    root.mainloop()                     # start the main loop of the window


if __name__ == "__main__":
    main()