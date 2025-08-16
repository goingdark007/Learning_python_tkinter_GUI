import tkinter as tk # imports tkinter gui

def print_name(): # Displays the entered text in the widget in console

    name = text.get("1.0", tk.END)  # Stores the user input in a variable
    # syntax is text.get("line_number.index", "line_number.index") like ("1.0", "2.3") it works like string slicing.
    # Note, /n is included too in the variable

    print(name)

window = tk.Tk() # .Tk class creates a root window

label = tk.Label( # Label is a widget that displays static text or image

    text ='Multiline Input',

    fg= 'white', # Set the text color to white

    bg= 'black', # Set the background color to black

)

text = tk.Text() # Creating a text widget for taking multiline inputs

# text widget comes with prefilled text
text.insert(tk.END,"Hello") # .insert() will insert text at the specified position if there’s already text at or after that position
# Or append text to the specified line if the character number is greater than the index of the last character in the text box.

text.insert(tk.END,"\nNazmul") # tk.END is used to automatically append any text at the last and \n is used to add a new line

button = tk.Button( # Clickable button widget

    text="Entry", # Displays the text in button

    command= print_name, # Command calls the function on clicked

)

label.pack() # to place the widget in the window.

text.pack()

button.pack()

window.mainloop() # .mainloop() runs the gui