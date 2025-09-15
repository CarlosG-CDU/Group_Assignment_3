#*****************
#   GUI page to handle UI
#   GUI.py
#*****************



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import AI_Stuff

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
        self.input_type = ttk.Combobox(self._root, values = ["Sentiment Model", "find_another_model"], state = "readonly")   # TODO need to rename the text menus
        self.input_type.set("Select Model")
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
        #self.output_label.config(text = "TODO model")
        user_input = self.input_text.get("1.0", tk.END).strip()
        print("User enterd: ", user_input)  #remove later
        selected_model = self.input_type.get()

        if selected_model == "Selected Model":  #check if a model has been selected
            self.output_label.config(text = "Please select a model from drop menu")
            return
        
        print(f"Selected model: {selected_model}") #debug

        print("Send data to AI_Stuff model")    #debug remove later
        try:
            if selected_model == "Sentiment Model":
                result = AI_Stuff.analyse_sentiment(user_input)
                print("Result from model = :", result)  #debug remoev later
                self.output_label.config(text = "Sentiment: " + result)
                
                
            elif selected_model == "find_another_model":
                print("Find another model")
                
            else:
                self.output_label.config(text = "Wrong model selected")     #should never get here but added just in case
        except Exception as e:
            self.output_label.config(text=f"Somethign is worng: {str(e)}")
            print(f"Error in run_model: {str(e)}")  # debug. show whats hanging the code

    def show_model_info(self):
        self.output_label.config(text = "The sentiment model will check any sentence you input into the text box and give an opinion if its Positive or Negative")

    def show_oop_explinations(self):
        self.output_label.config(text = "TODO OOP explinations")

    def creators(self):
        #self.output_label.config(text = "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        messagebox.showinfo("Creators", "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        

   