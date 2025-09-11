#GUI page to handle UI

import tkinter as tk

class HugFaceGui:
    def__init__(self, root):
        self._root = root   #this is encapsulation      
        self._root.title("Group 5 Assingment 3")
        self.setup_layout()
    
    def setup_layout(self):
        label = tk.Label(self._root,, text = "Welcome to Assignment 3")
        label.pack(padx = 10, pady = 10)