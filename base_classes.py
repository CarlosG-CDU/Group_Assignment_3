
#*****************
#Multiple Inheritance
#HugFaceGui, function from GUI.py uses GuiBase for window setup
#abandoned trying to have the messages come from here. 
#*****************

import tkinter as tk

class GuiBase:
    def __init__(self, window):
        self.window = window  # this saves the tkinter window
        self.window.title("Group 5 Assignment 3")  # can't think of a better name??

class AiModelBase:
    def __init__(self):
        self.__model_name = "No Model"

    def get_model_name(self):
        return self.__model_name
    
    def set_model_name(self, name):
        self.__model_name = name