
#*****************
#Multiple Inheritance
#HugFaceGui, function from GUI.py uses GuiBase for window setup
#abandoned trying to have the messages come from here. 
#*****************


import tkinter as tk

class GuiBase:          #use convention and start with uppercase as explained in class for a class
    def __init__(self, window):
        self.window = window  # this saves the tkinter window
        self.window.title("Group 5 Assignment 3")  # can't think of a better name??

class AiModelBase:      #use convention and start with uppercase as explained in class for a class
    def __init__(self, name = "No Model"):
        self.__model_name = name

    def run(self, input_text):
        return "Do nothin"
    
    