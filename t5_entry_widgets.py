import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

label = tk.Label( # Label is a widget that displays static text or image

    text ='Name',

    fg= 'white', # Set the text color to white

    bg= 'black', # Set the background color to black

)

entry = tk.Entry( # It’ll display a small text box that the user can type some text into

    fg="yellow", # Sets the input text color to yellow

    bg="blue", # Sets the background color to blue

    width=50 # sets the width of widget

)

label.pack() # to place the widget in the window.

entry.pack() # to place the widget in the window.

name = entry.get() # Stores the user input in a variable

window.mainloop() # .mainloop() runs the gui

print(name)