from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, Label
import shutil
import itertools
import os



IMAGE_FRAME_RATIO = 0.9



class DataManager():

    def __init__(self, root):
        self.data_a_path = "./data_a/"
        self.data_b_path = "./data_b/"
        self.results_path = "./results/"
        self.root = root
        self.current_image_index = 0


    def update_listbox(self, loaded_listbox, path):
        # UPDATE LISTBOX FUNCTION
        loaded_listbox.delete(0, tk.END)
        for file_name in os.listdir(path):
            loaded_listbox.insert(tk.END, file_name)
        loaded_listbox.update()

    def change_image(self, direction, processed_data_listbox, image_frame):
        
        current_index = processed_data_listbox.curselection()[0]        # Get the current selection index
        
        total_items = processed_data_listbox.size()                     # Get the total number of items in the listbox
        
        if direction == "right":                                        # Calculate the new index based on the direction
            new_index = (current_index + 1) % total_items
        elif direction == "left":
            new_index = (current_index - 1) % total_items
        
        processed_data_listbox.selection_clear(current_index)           # Update the selection in the listbox
        processed_data_listbox.selection_set(new_index)
        processed_data_listbox.activate(new_index)
        
        self.image_to_frame(image_frame, processed_data_listbox)        # Call the image_to_frame function to display the new image


    # --------------------------------------------------------------------#
    # --------------------- DATA LOAD/DELETE------------------------------#
    # --------------------------------------------------------------------#

    def load_data_a(self, loaded_data_a_listbox):
        print("A Loading data procedure started")
        file_paths = filedialog.askopenfilenames(initialdir = "/", title = "Select data A folder", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_paths: # if user selected a folder
            destination_path = self.data_a_path
            for file_path in file_paths:
                file_name = file_path.split("/")[-1]
                shutil.copy(file_path, destination_path + file_name) 
            
            # UPDATE LISTBOX FUNCTION
            self.update_listbox(loaded_data_a_listbox, self.data_a_path)

    def load_data_b(self, loaded_data_b_listbox):
        print("B Loading data procedure started")
        file_paths = filedialog.askopenfilenames(initialdir = "/", title = "Select data A folder", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_paths: # if user selected a folder
            destination_path = self.data_b_path
            for file_path in file_paths:
                file_name = file_path.split("/")[-1]
                shutil.copy(file_path, destination_path + file_name)
            
            # UPDATE LISTBOX FUNCTION
            self.update_listbox(loaded_data_b_listbox, self.data_b_path)

    def delete_data_a(self, loaded_data_a_listbox):
        print("A Deleting data procedure started")
        file_list = os.listdir(self.data_a_path)
        for file_name in file_list:
            file_path = os.path.join(self.data_a_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # UPDATE LISTBOX FUNCTION
        self.update_listbox(loaded_data_a_listbox, self.data_a_path)

    def delete_data_b(self, loaded_data_b_listbox):
        print("B Deleting data procedure started")
        file_list = os.listdir(self.data_b_path)
        for file_name in file_list:
            file_path = os.path.join(self.data_b_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # UPDATE LISTBOX FUNCTION
        self.update_listbox(loaded_data_b_listbox, self.data_b_path)

    def delete_data_results(self, processed_data_listbox):
        print("Deleting results procedure started")
        file_list = os.listdir(self.results_path)
        for file_name in file_list:
            file_path = os.path.join(self.results_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # UPDATE LISTBOX FUNCTION
        self.update_listbox(processed_data_listbox, self.results_path)

    # --------------------------------------------------------------------#
    # ----------- RESULTS DATA --> IMAGE FRAME transport------------------#
    # --------------------------------------------------------------------#

    def image_to_frame(self, image_frame,  processed_data_listbox):
        index = processed_data_listbox.curselection()[0]                      # Get selected line index
        filename = processed_data_listbox.get(index)                          # Get the line's text
        file_path = os.path.abspath(os.path.join(self.results_path, filename))     # Get the absolute file path

        # IMAGE RESIZE logic to the frame size
        img = Image.open(file_path)
        frame_width = image_frame.winfo_width()
        frame_height = image_frame.winfo_height()
        #----
        img_ratio = img.width / img.height
        frame_ratio = frame_width / frame_height

        if frame_ratio > img_ratio:
            width = int(frame_height * img_ratio * IMAGE_FRAME_RATIO)
            height = int(frame_height * IMAGE_FRAME_RATIO)
        else:
            width = int(frame_width * IMAGE_FRAME_RATIO)
            height = int(frame_width / img_ratio * IMAGE_FRAME_RATIO)
        #----
        img = img.resize((width, height))

        photo = ImageTk.PhotoImage(img)

        image_label = Label(self.root, image=photo)
        image_label.image = photo
        image_label.grid(row=2, column=1)

        