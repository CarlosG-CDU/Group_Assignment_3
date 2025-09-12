#*****************
#   main page.
#   main.py
#*****************

#this serves as the main loop and seperately calling functions
#this is a requirement of assignment

import tkinter as tk
from GUI import HugFaceGui

def main():
    root = tk.Tk()
    app = HugFaceGui(root)          #goto GUI page to do GUI stuff
    root.mainloop()

if __name__ == "__main__":
    main()