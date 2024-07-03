from tkinter import filedialog
import tkinter as tk
import shutil
import os
import webbrowser
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import imageio
from tkinter import filedialog, messagebox
from PIL import Image


DIALOG_FONT_A = ('Helvetica', 10, "bold")


class ProcessingManager():


    def __init__(self, root, data_a, data_b, results_listbox):
        self.root = root
        self.data_a = data_a                    # listbox a
        self.data_b = data_b                    # listbox b
        self.results_listbox = results_listbox  # processed_listbox

        self.data_a_path = "./data_a/"
        self.data_b_path = "./data_b/"
        self.results_path = "./results/"

    
    def update_processed_data(self):
        # UPDATE LISTBOX FUNCTION
        self.results_listbox.delete(0, tk.END)
        for file_name in os.listdir(self.results_path):
            self.results_listbox.insert(tk.END, file_name)
        self.results_listbox.update()

    def open_file(self):
        index = self.results_listbox.curselection()[0]                      # Get selected line index
        filename = self.results_listbox.get(index)                          # Get the line's text
        file_path = os.path.abspath(os.path.join(self.results_path, filename))               # Get the absolute file path
        
        if os.path.isfile(file_path):                                       # Check if file exists
            os.startfile(file_path)                                         # Open the file in default program
        else:
            print(f"File {file_path} does not exist.")
        
    def process_data(self, selection_2D_image, selection_2D_CT_scan, selection_FF, selection_4):
        # DATA processing according to selection
        processes = [selection_2D_image, selection_2D_CT_scan, selection_FF, selection_4]
        if selection_2D_image.get():
            print("Processing 2D image")
            self.proces_2D_image()
        elif selection_2D_CT_scan.get():
            print("Processing 2D CT scan")
            self.proces_2D_CT_scan()
        elif selection_FF.get():
            print("Processing FF")
            self.proces_FF()
        elif selection_4.get():
            print("Processing option 4")
            self.proces_4()
        
    def proces_2D_image(self):
        # ---------------------- File selection logic  ------------------------#
        try:                                                                    # file selection, depending which listbox A or B was selected
            selected_file = self.data_a.get(self.data_a.curselection())            
        except:
            selected_file = self.data_b.get(self.data_b.curselection())
        
        print("Processing 2D image: ", selected_file)
        
        if os.path.exists(os.path.join(self.data_a_path, selected_file)):
            file_path = os.path.join(self.data_a_path, selected_file)           # defining the file path
            print(f"Processing from file A")
        else:
            file_path = os.path.join(self.data_b_path, selected_file)
            print(f"Processing from file B")

        # ---------------------- 2D image processing script ------------------------#
        pixel_values = np.loadtxt(file_path)                                    # load pixel values from the file
        fig, ax = plt.subplots()                                                # create a figure and axis
        
        img = ax.imshow(pixel_values, cmap='viridis')                           # plot the pixel values as an image
        cbar = fig.colorbar(img)                                                # add a colorbar to the image
        
        # adjust th evisual properties of the graph
        ax.set_title('Pixel Values')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        cbar.set_label('Intensity')
        
        # ---------------------- File needs to be saved in results listbox  ------------------------#
        # Save processed file as a .png
        save_path = os.path.join(self.results_path, selected_file.split('.')[0] + '.png')
        plt.savefig(save_path)
        print(f"Processed file saved as {save_path}")

        # ------------------------------------------------------------------------- # 
        # show plot after plt.savefig NEEDED -> figure shown cannot be reused in code
        plt.show()
        self.update_processed_data()

    def proces_2D_CT_scan(self):
        # ---------------------- LISTBOX SELECTION LOGIC ------------------------#
        dialog = tk.Toplevel()
        dialog.geometry("300x150")          # Set the minimum size of the dialog window
        dialog.update_idletasks()           # Update the dialog window to get its actual size
        
        choice = tk.StringVar()

        tk.Label(dialog, text="Select the data source:", font=DIALOG_FONT_A).pack(pady=12)
        tk.Radiobutton(dialog, text="Gif from datapack A", variable=choice, value="A").pack()
        tk.Radiobutton(dialog, text="Gif from datapack B", variable=choice, value="B").pack()
        tk.Button(dialog, text="OK", command=dialog.destroy).pack(pady=10)
        dialog.wait_window()
        print("dialog option - chosen")

        if choice.get() == "A":
            selected_listbox = self.data_a 
        else:
            selected_listbox = self.data_b 
        
        # ---------------------- GIF FORMATION LOGIC  ------------------------#
        # A) INDIVIDUAL PNGs generation to from selected listbox to the gif_processing folder
        len_files = len(selected_listbox.get(0, tk.END))
    
        for step in range(len_files):
            file_path = os.path.join(self.data_a_path if selected_listbox == self.data_a else self.data_b_path, selected_listbox.get(step))
            pixel_values = np.loadtxt(file_path)

            # Create a figure and axis
            fig, ax = plt.subplots()
            # Display the pixel values as an image
            img = ax.imshow(pixel_values, cmap='viridis')
            # Add a colorbar for reference
            cbar = fig.colorbar(img)

            # Adjust the visual properties
            ax.set_title('Pixel Values')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            cbar.set_label('Intensity')

            plt.savefig(f"./gif_processing/{selected_listbox.get(step).split('.')[0]}.png")
            plt.close()
            # we have individual PNGs in a folder gif_processing
        
        # B) GIF formation from the folder gif_processing and saving to processed_listbox
        images = []
        for file_name in os.listdir("./gif_processing"):
            if file_name.endswith(".png"):
                file_path = os.path.join("./gif_processing", file_name)
                images.append(imageio.imread(file_path))

        gif_path = os.path.join(self.results_path, "animated.gif")
        imageio.mimsave(gif_path, images, duration=0.5)

        # C) CLEAR the gif_processing folder
        folder_path = "./gif_processing"
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        self.update_processed_data()

    def proces_FF(self):
        ...

    def proces_4(self):
        ...