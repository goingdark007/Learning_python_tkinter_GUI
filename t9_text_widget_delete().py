import tkinter as tk # imports tkinter gui

def print_name(): # Displays the entered text in the widget in console

    name = text.get("1.0", tk.END)  # Stores the user input in a variable
    # syntax is text.get("line_number.index", "line_number.index") like ("1.0", "2.3") it works like string slicing.
    # Note, /n is included too in the variable

    print(name)

def delete_name(): # To delete the entered text in the text widget

    text.delete("1.0", tk.END) # .delete() is also similar to get syntax it works like string slicing
    # Note /n can be deleted too, making the second line into first line

window = tk.Tk() # .Tk class creates a root window

label = tk.Label( # Label is a widget that displays static text or image

    text ='Multiline Input',

    fg= 'white', # Set the text color to white

    bg= 'black', # Set the background color to black

)

text = tk.Text() # Creating a text widget for taking multiline inputs

button = tk.Button( # Clickable button widget

    text="Entry", # Displays the text in button

    command= print_name, # Command calls the function on clicked

)

button2 = tk.Button(

    text="Delete",

    command= delete_name, # Command calls the function on clicked

)

label.pack() # to place the widget in the window.

text.pack()

button.pack()

button2.pack()

window.mainloop() # .mainloop() runs the gui