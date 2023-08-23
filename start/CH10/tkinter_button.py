# Seconder tkinter script
# Add a button and command
# Created by Jac 8/22/2023 

# Import tkinter
from tkinter import *
from tkinter import messagebox

# Functions
def button_clicked():
    Label(window, text = "button was clicked").pack()
    messagebox.showerror("Error", "Don't click that")

# Create the GUI main window
window = Tk()
window.title("Hello Python")
window.geometry('300x200')

# Add widgets
lbl = Label(window, text="Hello, world")

    #Button Widget
button = Button(window, text = "click Here", command = button_clicked)
button.pack()

# Enter the main event loop
window.mainloop()