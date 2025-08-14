import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

label = tk.Label(

    text ='Hello, Tkinter',

    fg= 'white', # Set the text color to white

    # You can also use hexadecimal RGB values to set the color

    bg= 'black', # Set the background color to black

    width= 10, # Sets the width of the widget

    height= 10 # sets the height of the widget

) # Label is a widget that displays static text or image

label.pack() # to place the widget in the window.

window.mainloop() # .mainloop() runs the gui