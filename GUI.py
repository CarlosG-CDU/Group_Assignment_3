#*****************
#   GUI page to handle UI
#   GUI.py
#*****************



import tkinter as tk
from tkinter import ttk

class HugFaceGui:
    def __init__(self, root):
        self._root = root   # Save the root window in a variable internally     
        self._root.title("Group 5 Assingment 3")        #title for the GUI box
        self.setup_layout()
  
#    def setup_layout(self):
#        label = tk.Label(self._root, text = "Welcome to Assignment 3")
#        label.pack(padx = 10, pady = 10)

    def setup_layout(self):   
        
        ###Drop down menu / text box for input
        self.input_type = ttk.Combobox(self._root, values = ["Text select 1", "Text Selct2"], state = "readonly")   # TODO need to rename the text menus
        self.input_type.set("Text")
        self.input_type.grid(row = 0, column = 0, padx = 5, pady = 5)

        ###Text input
        self.input_text = tk.Text(self._root, height = 5, width = 50)
        self.input_text.grid(row = 1, column = 0, padx = 5, pady = 5 )

        ###Run / go button
        tk.Button(self._root, text = "Run Model", command = self.run_model).grid(row = 2, column = 0, padx = 5, pady = 5) 

        ###Output text box
        self.output_label = tk.Label(self._root, text = "Output stuff will be shonw here", wraplength = 400)
        self.output_label.grid(row = 3, column = 0, padx = 5, pady = 5)

        ###info and explinations button
        tk.Button(self._root, text = "Model Info", command = self.show_model_info).grid(row = 4, column = 0, padx = 5, pady = 5) 
        tk.Button(self._root, text = "OOP Explinations", command = self.show_oop_explinations).grid(row = 5, column = 0, padx = 5, pady =5)

        ###made by button
        tk.Button(self._root, text = "Created by", command = self.creators).grid(row = 6, column = 0, padx = 5, pady = 5) 
        

    def run_model(self):
        self.output_label.config(text = "TODO model")

    def show_model_info(self):
        self.output_label.config(text = "TODO model info")

    def show_oop_explinations(self):
        self.output_label.config(text = "TODO OOP explinations")

    def creators(self):
        self.output_label.config(text = "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        

   