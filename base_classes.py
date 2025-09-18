
#*****************
#Multiple Inheritance
#HugFaceGui, function from GUI.py uses GuiBase for window setup
#abandoned trying to have the messages come from here. 

import tkinter as tk

class GuiBase:
    def __init__(self, window):
        self.window = window  # this saves the tkinter window
        self.window.title("Group 5 Assignment 3")  # can't think of a better name??

