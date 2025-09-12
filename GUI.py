#GUI page to handle UI

import tkinter as tk
from tkinter import ttk

class HugFaceGui:
    def __init__(self, root):
        self._root = root   # Store the root window (protected attribute by convention)     
        self._root.title("Group 5 Assingment 3")
        self.setup_layout()
  
#    def setup_layout(self):
#        label = tk.Label(self._root, text = "Welcome to Assignment 3")
#        label.pack(padx = 10, pady = 10)

    def setup_layout(self):     
        ###Drop down menu / box for input
        self.input_type = ttk.Combobox(self._root, values = ["Text", "Image prompt"], state = "readonly")   
        self.input_type.set("Text")
        self.input_type.grid(row = 0, column = 0, padx = 5, pady = 5)

        ###Text input
        self.input_text = tk.Text(self._root, height = 5, width = 50)
        self.input_text.grid(row = 1, column = 0, padx = 5, pady = 5)

       
        