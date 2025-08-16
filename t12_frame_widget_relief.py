import tkinter as tk # imports tkinter gui

border_effects = { # A dictionary for storing relief methods

    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,
}

window = tk.Tk() # .Tk class creates a root window

for relief_name, relief in border_effects.items(): # Using .items() takes the key and value of the dictionary for each iteration

    frame = tk.Frame(master=window, relief=relief, borderwidth=5) # declares parent container, relief sets the border style
    # and sets the borderwidth to 5 pixels

    frame.pack(side=tk.LEFT) # using the pack geometry manager, left-to-right stacking

    label = tk.Label(master=frame, text=relief_name) # Created a label widget which shows relief name

    label.pack() # to place the widget in the window.

window.mainloop() # .mainloop() runs the gui