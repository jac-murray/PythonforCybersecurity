# First tkinter script
# Create by Jac 8/22/2023

# Import tkinter
from tkinter import *

# Create the GUI main window
window = Tk()
window.title("Hello Python")
window.geometry('300x200')

# Add widgets
lbl = Label(window, text="Hello, world")
lbl.grid(column=0, row=0)

# Enter the main event loop
window.mainloop()