import tkinter as tk # imports tkinter gui

def print_name(): # Displays the entered text in the widget in console

    name = entry.get()  # Stores the user input in a variable

    print(name)

def delete_name(): # To delete the entered text in the widget

    entry.delete(0, tk.END) # .delete(0,4) works like string slicing will delete everything from
    # O index to 4 index and tk.END is the last index of the string

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

button2 = tk.Button(

    text="Delete",

    command= delete_name, # Command calls the function on clicked

)

label.pack() # to place the widget in the window.

entry.pack()

button.pack()

button2.pack()

window.mainloop() # .mainloop() runs the gui