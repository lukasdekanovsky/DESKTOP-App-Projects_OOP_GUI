from tkinter import filedialog

class FileManager():

    def __init__(self):
        self.file_path = ""

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
