#*****************
#   GUI page to handle UI
#   GUI.py
#*****************


from AI_Stuff import SentimentModel, TextToImageModel
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import AI_Stuff
from base_classes import GuiBase, AiModelBase         #this imports the parent class from base_classes.py
from PIL import Image, ImageTk                        #this imports image module compatible with tkinter
import os
import threading
#Ref- https://docs.python.org/3/library/threading.html                              


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
             self.output_label.config(text=f"{choice} selected", foreground = "black")
             print(f"Selected model updated: {choice}")# Debug 
        else:
            self.output_label.config(text="Please select a model from the dropdown menu")
            print("No valid model selected")


#    def setup_layout(self):
#        label = tk.Label(self._root, text = "Welcome to Assignment 3")
#        label.pack(padx = 10, pady = 10)

    def setup_layout(self):   
        
        Button_frame = tk.LabelFrame(self.window, bg="pink", width=1200, height=1000)    #use to call all buttons into frame for neat GUI display
        Button_frame.grid(row=1, column=0, padx=10, pady=10)
        
        ###Drop down menu / text box for input
        self.input_type = ttk.Combobox(Button_frame, font=("New Times Roman", 10), values = ["Sentiment Model", "Text to Image"], state = "readonly")   # TODO need to rename the text menus
        self.input_type.set("Select Model Here")
        self.input_type.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.input_type.bind("<<ComboboxSelected>>", self.update_selected_model)

        ###Text input
        self.input_text = tk.Text(Button_frame, height = 5, width = 50)
        self.input_text.grid(row = 1, column = 0, padx = 5, pady = 5 )


        ###Run / go button
        tk.Button(Button_frame, bg="green", text = "Run Model", command = self.run_model).grid(row = 2, column = 0, padx = 5, pady = 5, sticky='e') 

        ###Output text box
        self.output_label = tk.Label(self.window, text = "Please select a model from the dropdown menu", font=("Verdana", 10), wraplength = 400)
        self.output_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky='w')

        ###info and explinations button
        tk.Button(Button_frame, text = "Model Info", command = self.show_model_info).grid(row = 4, column = 0, padx = 5, pady = 5, sticky='w') 
        tk.Button(Button_frame, text = "OOP Explinations", command = self.show_oop_explinations).grid(row = 5, column = 0, padx = 5, pady =5, sticky='w')

        ###made by button
        tk.Button(Button_frame, text = "Created by", command = self.creators).grid(row = 6, column = 0, padx = 5, pady = 5, sticky='w')

        #create frame for image
        image_frame = tk.LabelFrame(Button_frame, bg="lightblue", text="Image will open here", width=300, height=300)
        image_frame.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        self.image_label = tk.Label(image_frame)                #pack image as label inside frame using pillow module
        self.image_label.grid(row=5, column=1, padx=5, pady=5)  

        #create radio buttons
        r = tk.IntVar()  #define variable r
        r.set(2) #set save image as the default
        #r.get()

        #radio_frame = tk.Frame(self._root)

        def click_rb(value):   #https://www.geeksforgeeks.org/python/save-image-to-file-in-python-using-tkinter/
           if value == 1:
             self.open_image()
           elif value == 2:
               self.save_image()
             

        rb = tk.Radiobutton(Button_frame, text="Open Image", variable=r, value=1, command=lambda: click_rb(r.get()))   #.pack(row=3, column=2)  #radio button #command=lambda: click_rb(r.get())
        rb2 = tk.Radiobutton(Button_frame, text="Save Image", variable=r, value=2, command=lambda: click_rb(r.get()))    #.pack(row=4, column=2)

        rb.grid(row=1, column=2)
        rb2.grid(row=2, column=2)          
        
        rbLabel = tk.Label(Button_frame, bg="lightblue", text="Please make a selection")
        rbLabel.grid(row=0, column=2)

        ###Progress bar
        #Ref- https://www.pythontutorial.net/tkinter/tkinter-progressbar/
        #Ref- https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar
        self.progress = ttk.Progressbar(self.window, mode="indeterminate", length=250)
        self.progress.grid(row=7, column=0, padx=5, pady=5)
        self.progress.grid_remove()

    def run_model(self):
        user_text = self.input_text.get("1.0", tk.END).strip()
        if not self.__selected_model:
            self.output_label.config(text="Please select a model from the dropdown menu")
            return
        if not user_text:
            self.output_label.config(text="Please enter some text first")
            return
           
        choice = self.input_type.get()
        self.output_label.config(text=f"{choice} running... please wait")

        ###Show the progress bar
        self.progress.grid()
        self.progress.start(12) # speed of animation adjust if needed

        ###Do the long work in the background thread
        def _worker():
            try:
                result = self.__selected_model.run(user_text)
                err = None
            except Exception as e:
                result, err = None, e
        # return to UI thread to update widgets
            self.window.after(0, lambda: self._finish_run(choice, result, err))

        threading.Thread(target=_worker, daemon=True).start()

    def _finish_run(self, choice, result, err):
        self.progress.stop()
        self.progress.grid_remove()

        if err:
            self.output_label.config(text=f"Something went wrong: {err}", foreground="black") 
            print("Error in run_model:", err) 
        else:
            print("This is the result: ", result)

            #time execution on GUI interface
            secs = getattr(self.__selected_model, "_last_run_seconds", None)
            if isinstance(secs, (int, float)):
                result = f"{result}  (took {secs:.2f}s)"

            if choice == "Sentiment Model":
                if "POSITIVE" in result:
                    self.output_label.config(text = result, foreground = "green")       #happy print green
                elif "NEGATIVE" in result:
                    self.output_label.config(text=result, foreground="red")             #sad print red
                else:
                    self.output_label.config(text=result, foreground="black")  # Default colour for other results

            elif choice == "Text to Image":
                #reset label for text to image completion
                self.output_label.config(text=result, foreground="black")

            print("Result from model:", result)

    
    def open_image(self):
        try:               # Check if image was saved
                
            if not os.path.exists("output.png"):
                self.output_label.config(text="Image file not found: output.png")
                print("Image file output.png not found!")
                return
            
            image = Image.open("output.png")    #opens the image
            image = image.resize((256, 256), resample=Image.Resampling.LANCZOS)        #resize
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        

        except Exception as e:
                self.output_label.config(text=f"Failed to load image: {e}")
                print("Image load error:", e)

        else:       #just incase we end up here unexpectedly
            self.output_label.config(text = "Please select a model from drop menu")     # only will get here if no model selected
                
        
         #Exception as err:    #something is broken
            #self.output_label.config(text=f"Somethign is wrong: {str(err)}")
            #print(f"Error in run_model: {str(err)}")  # debug. show whats hanging the code

    def save_image(self):
        if os.path.exists("output.png"):
            new_name = "saved_output.png"
            Image.open("output.png").save(new_name)


    
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
        explinations = """
    * Multiple Inheritance: 
    HugFaceGui uses GuiBase for window setup

    * Encapsulation: 
    is used by making self.__root and self.__selected model private with meathods get_model and set_model for safety

    * Method Overriding:
    - AIModelBase defines a run() method that does nothing.
    - SentimentModel overrides run() to analyse text sentiment.
    - TextToImageModel overrides run() to generate images.
    - This shows how child classes replace the parent's method with their own specialised version.

    * Polymorphism: 
    AiModelBase has a basic run() method that does nothing. 
    - SentimentModel changes it to check if text is positive or negative using DistilBERT. 
    - TextToImageModel changes it to make pictures with Stable Diffusion, saving them as "output.png". 
    - HugFaceGui calls run() on the selected model, and it works differently without needing to know what model it is

    * Multiple Decorators: 
    - In AI_Stuff.py, each run() method is decorated with @log_call and @timeit together. 
    - This means when run() is called, first it is logged (with a spinner), then the execution time is measured, before finally running the real function.
                                                   
    """
               
 
        #self.output_label.config(text = "explinations", wraplength = 400)
        messagebox.showinfo("OOP Explanations", message=explinations, parent=self.window)


    def creators(self):
        #self.output_label.config(text = "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")
        messagebox.showinfo("Creators", "Made by Carlos Galli, Cody Old and Lauren Whitford S2 - 2025")