# GUI Example 3
# This program demonstrates a simple Tkinter GUI window.
# Note: This will open a GUI window when executed.

import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("GUI Example 3")

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# root.mainloop()
