import tkinter as tk
from GUIdraft import HugFaceGui

def main():
    root = tk.Tk()
    app = HugFaceGui(root)          #goto GUI page to do GUI stuff
    root.mainloop()


if __name__ == "__main__":
    main()