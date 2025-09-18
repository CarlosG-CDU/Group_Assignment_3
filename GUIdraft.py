
#created a copy of everything o I could play around
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Ai_draft_loz

class HugFaceGui:
    def __init__(self, root):
        self.selected_model = None
        self._root = root   # Save the root window in a variable internally     
        self._root.title("Group 5 Assingment 3")        #title for the GUI box
        self.setup_layout()
        root.geometry("600x600")
  
#    def setup_layout(self):
#        label = tk.Label(self._root, text = "Welcome to Assignment 3")
#        label.pack(padx = 10, pady = 10)

    def setup_layout(self):   
        
        ###Drop down menu / text box for input
        self.input_type = ttk.Combobox(self._root, values = ["Sentiment Model", "Text to Image"], state = "readonly")   # TODO need to rename the text menus
        self.input_type.set("Select Model Here")
        self.input_type.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.input_type.bind("<<ComboboxSelected>>", self.update_selected_model)

        ###Text input
        self.input_text = tk.Text(self._root, height = 5, width = 50)
        self.input_text.grid(row = 1, column = 0, padx = 5, pady = 5 )

        ###Run / go button
        tk.Button(self._root, text = "Run Model", command = self.run_model).grid(row = 2, column = 0, padx = 5, pady = 5) 

        ###Output text box
        self.output_label = tk.Label(self._root, text = "Please be patient. Some models may take upto 5 minutes to work", wraplength = 400)
        self.output_label.grid(row = 3, column = 0, padx = 5, pady = 5)

        ###info and explinations button
        tk.Button(self._root, text = "Model Info", command = self.show_model_info).grid(row = 4, column = 0, padx = 5, pady = 5) 
        tk.Button(self._root, text = "OOP Explinations", command = self.show_oop_explinations).grid(row = 5, column = 0, padx = 5, pady =5)

        ###made by button
        tk.Button(self._root, text = "Created by", command = self.creators).grid(row = 6, column = 0, padx = 5, pady = 5) 

    def update_selected_model(self, event=None):    #update the slected modle here
        self.selected_model = self.input_type.get()
        print(f"Selected model updated: {self.selected_model}")  # Debug to confirm selection


    def run_model(self):        #get the users input from the text box
        #self.output_label.config(text = "TODO model")
        user_text = self.input_text.get("1.0", tk.END).strip()
        print("User entered: ", user_text)  #remove later used to verify the input text
        self.selected_model = self.input_type.get()

        if self.selected_model == "Selected Model":  #check if a model has been selected
            self.output_label.config(text = "Please select a model from drop menu")
            return
        
        print(f"Selected model: {self.selected_model}") #debug

        #self.output_label.config(text="Processing, please wait...")
        # Reset the output label with model-specific processing message
        if self.selected_model == "Sentiment Model":
            self.output_label.config(text="Analyzing sentiment, please wait...")
        elif self.selected_model == "Text to Image":
            self.output_label.config(text="Generating image, please wait (up to 5 minutes)...")
        self._root.update()


        print("Send data to AI_Stuff model")    #debug remove later
        try:
            if self.selected_model == "Sentiment Model":     #call Sentiment Model function
                result = Ai_draft_loz.analyse_sentiment(user_text)
                print("Result from model = :", result)  #debug remoev later
                self.output_label.config(text=f"sentiment: {result}")
                
            elif self.selected_model == "Text to Image":        #call text to image
                #self.output_label.config(text = "please be patient. this can take up to 5 minutes")
                result = Ai_draft_loz.text_to_image(user_text)
                
                self.output_label.config(text="Text to Image")
                #self.output_label.config(text=f"savedTo: {result}")
                self.output_label.config(text = f"Your Image saved as output.png")
                
            else:       #just incase we end up here unexpectedly
                self.output_label.config(text = "Please select a model from drop menu")     # only will get here if no model selected
                
        except Exception as err:    #something is broken
            self.output_label.config(text=f"Somethign is wrong: {str(err)}")
            print(f"Error in run_model: {str(err)}")  # debug. show whats hanging the code

    def show_model_info(self):      #display info about selected model
        self.selected_model = self.input_type.get() #show current selection
        #self.output_label.config(text = "The sentiment model will check any sentence you input into the text box and give an opinion if its Positive or Negative")
        if self.selected_model == "Select Model Here":
            self.output_label.config(text="Please select a model from the dropdown menu")
        
        elif self.selected_model == "Sentiment Model":
            self.output_label.config(text="The sentiment model analyses the input text and determines if it has a positive or negative sentiment.")
            print("Sentiment Model selected")  # Debug
        
        elif self.selected_model == "Text to Image":
            self.output_label.config(text="This model will provide a picture from the text provided by the end user. Provide a brief description of the image you would like to see. For example: 'A red lady bug on a flower'")
            print("Text to Image")  # Debug
        
        else:
            self.output_label.config(text="Unknown model selected")
            print("Unknown model selected")  # Debug
    

    def show_oop_explinations(self):
        self.output_label.config(text = "TODO OOP explinations")

    def creators(self):
        #self.output_label.config(text = "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        messagebox.showinfo("Creators", "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        

    

