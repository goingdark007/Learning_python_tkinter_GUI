import tkinter as tk # imports tkinter gui

def print_name(): # Displays the entered text in the widget in console

    name = entry.get()  # Stores the user input in a variable

    print(name)

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

button = tk.Button( # Clickable button widget

    text="Entry", # Displays the text in button

    command= print_name, # Command calls the function on clicked

)

label.pack() # to place the widget in the window.

entry.pack()

button.pack()

window.mainloop() # .mainloop() runs the gui