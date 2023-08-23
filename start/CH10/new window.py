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

def show_joke_window():
    joke_text = get_random_joke()
    
    joke_window = tk.Toplevel(root)
    joke_window.title("Dad Joke")
    
    joke_label = tk.Label(joke_window, text=joke_text, wraplength=300, justify="center")
    joke_label.pack(padx=20, pady=20)

# Create the main window
root = tk.Tk()
root.title("Dad Joke Viewer")
root.geometry('350x200')

# Create a button to get and display a joke in a new window
get_joke_button = tk.Button(root, text="Get a Dad Joke", command=show_joke_window)
get_joke_button.pack()

# Start the Tkinter event loop
root.mainloop()
