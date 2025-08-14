import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

button = tk.Button( # Clickable button widget

    text="Click me!", # Displays the text

    width=25, # Sets the width of the widget

    height=5, # Sets the height of the widget

    bg="blue", # Sets the background color to blue

    fg="yellow", # Sets the text color to yellow
)

button.pack() # to place the widget in the window.

window.mainloop() # .mainloop() runs the gui