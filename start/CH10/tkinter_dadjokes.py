# third tkinter script
# Dad joke
# Create by Jac 8/22/2023 

import tkinter as tk
import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        joke = data["joke"]
        return joke

def show_joke():
    joke_text = get_random_joke()
    joke_label.config(text=joke_text)

# Create the main window
window = tk.Tk()
window.title("Dad Joke Viewer")
window.geometry('350x200')

# Create a label for the joke
joke_label = tk.Label(window, text="", wraplength=300, justify="center")
joke_label.pack(padx=20, pady=20)

# Create a button to get and display a joke
get_joke_button = tk.Button(window, text="Get a Dad Joke", command=show_joke)
get_joke_button.pack()

# Start the Tkinter event loop
window.mainloop()