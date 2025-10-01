#*****************
#   main page.
#   main.py
#*****************


#######
#MUST RUN THE PROG FROM THIS PAGE
#######

import tkinter as tk
from GUI import HugFaceGui

def main():
    root = tk.Tk()
    app = HugFaceGui(root)          #goto GUI page to do GUI stuff
    root.mainloop()


if __name__ == "__main__":
    main()

    
