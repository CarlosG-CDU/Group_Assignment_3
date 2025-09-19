#*****************
#   GUI page to handle UI
#   GUI.py
#*****************


from AI_Stuff import SentimentModel, TextToImageModel
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import AI_Stuff
from base_classes import GuiBase, AiModelBase     #this improts the parent class from base_classes.py


class HugFaceGui(GuiBase, AiModelBase):   #HugFaceGui now inherits from both guibase
    def __init__(self, root):

        GuiBase.__init__(self, root)    #set up the GUI stuff
        AiModelBase.__init__(self)      #init AI Model Base
        
        self.__root = root  #encapsulation, hiding the variable for safety
        #self.selected_model = "No model"
        ##self.__selected_model = self.model_name     #use the inherited model name
        self.__selected_model = None
        self.models = {
            "Sentiment Model": SentimentModel(),
            "Text to Image": TextToImageModel()
        }
        #self._root = root   # Save the root window in a variable internally   handled by base_classes  
        #self._root.title("Group 5 Assingment 3")        #title for the GUI box this is now hangled by base_classes.py
        self.setup_layout()

    def get_root(self): #Get the Window
        return self.__root
    
    def get_model(self):    #Get the selected model
        return self.__selected_model
    
    def set_model(self, model): #set the selected model
        self.__selected_model = model

    def update_selected_model(self, event=None):
        choice = self.input_type.get()
        self.__selected_model = self.models.get(choice, None)

        if self.__selected_model:
             
             choice = self.input_type.get()
             self.output_label.config(text=f"{choice} selected")
             print(f"Selected model updated: {choice}")# Debug 
        else:
            self.output_label.config(text="Please select a model from the dropdown menu")
            print("No valid model selected")


#    def setup_layout(self):
#        label = tk.Label(self._root, text = "Welcome to Assignment 3")
#        label.pack(padx = 10, pady = 10)

    def setup_layout(self):   
        
        ###Drop down menu / text box for input
        self.input_type = ttk.Combobox(self.window, values = ["Sentiment Model", "Text to Image"], state = "readonly")   # TODO need to rename the text menus
        self.input_type.set("Select Model Here")
        self.input_type.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.input_type.bind("<<ComboboxSelected>>", self.update_selected_model)

        ###Text input
        self.input_text = tk.Text(self.window, height = 5, width = 50)
        self.input_text.grid(row = 1, column = 0, padx = 5, pady = 5 )

        ###Run / go button
        tk.Button(self.window, text = "Run Model", command = self.run_model).grid(row = 2, column = 0, padx = 5, pady = 5) 

        ###Output text box
        self.output_label = tk.Label(self.window, text = "Please select a model from the dropdown menu", wraplength = 400)
        self.output_label.grid(row = 3, column = 0, padx = 5, pady = 5)

        ###info and explinations button
        tk.Button(self.window, text = "Model Info", command = self.show_model_info).grid(row = 4, column = 0, padx = 5, pady = 5) 
        tk.Button(self.window, text = "OOP Explinations", command = self.show_oop_explinations).grid(row = 5, column = 0, padx = 5, pady =5)

        ###made by button
        tk.Button(self.window, text = "Created by", command = self.creators).grid(row = 6, column = 0, padx = 5, pady = 5) 

    def run_model(self):
        user_text = self.input_text.get("1.0", tk.END).strip()
        if not self.__selected_model:
            self.output_label.config(text="Please select a model from the dropdown menu")
            return
        
        choice = self.input_type.get()
        print(f"User Entered: {user_text}")     #debug to remove used to be user_text
        print(f"Selected model: {choice}") 

        try:
            result = self.__selected_model.run(user_text)
            self.output_label.config(text=result)
            print("Result from model: ", result)
        except Exception as err:
            self.output_label.config(text=f"Something went wrong: {str(err)}")
            print(f"Error in run_model: {str(err)}")


    def show_model_info(self):      #display info about selected model
        self.selected_model = self.input_type.get() #show current selection
        #self.output_label.config(text = "The sentiment model will check any sentence you input into the text box and give an opinion if its Positive or Negative")
        if self.selected_model == "Select Model Here":
            self.output_label.config(text="Please select a model from the dropdown menu")
        
        elif self.selected_model == "Sentiment Model":
            self.output_label.config(text="The sentiment model analyses the input text and determines if it has a positive or negative sentiment.")
            print("Sentiment Model selected")  # Debug
        
        elif self.selected_model == "Text to Image":
            self.output_label.config(text="This model will provide a picture from the text provided by the end user. The more info that is provided the better the result. You can over do it though. An example instruction A red lady bug on a flower")
            print("Text to Image")  # Debug
        
        else:
            self.output_label.config(text="Unknown model selected")
            print("Unknown model selected")  # Debug
    

    def show_oop_explinations(self):
        explinations = """Multiple Inheritance: HugFaceGui uses GuiBase for window setup
                          Encapsulation: is used by making self.__root and self.__selected model private with meathods get_model and set_model for safety
                          Polymorphism: AiModelBase has a basic run() method that does nothing. 
                    SentimentModel changes it to check if text is positive or negative using DistilBERT. 
                    TextToImageModel changes it to make pictures with Stable Diffusion, saving them as "output.png". 
                    HugFaceGui calls run() on the selected model, and it works differently without needing to know what model it is
                                                   
                          """
        #self.output_label.config(text = "explinations", wraplength = 400)
        messagebox.showinfo("OOP Explanations", message=explinations, parent=self.window)


    def creators(self):
        #self.output_label.config(text = "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        messagebox.showinfo("Creators", "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        

   