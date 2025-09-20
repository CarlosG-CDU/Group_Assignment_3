import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Test")
root.geometry("400x400")

# Load and display image
image = Image.open("output.png")
image = image.resize((256, 256))  # Resize for testing
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.image = photo  # Prevent garbage collection
image_label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
