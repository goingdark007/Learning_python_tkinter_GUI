import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

def handle_click(event): # Event handler. tkinter automatically passes an event object to the
    # function when something happens

    print("The button was clicked!") # it prints button was clicked

button = tk.Button(text="Click me!") # Creates a button widget with a text

button.bind("<Button-1>", handle_click) # When the user left-clicks on this button, calls
# the function handle_click. "<Button-2>" for middle mouse button, "<Button-3>" for right mouse button

button.pack() # to place the button widget in the window

window.mainloop() # .mainloop() runs the gui