import tkinter as tk # imports tkinter gui

def increase(): # Event handler function to increase the value

    value = int(lbl_value["text"]) # By writing ["text"] accesses the label widgets value and converts it to int

    lbl_value["text"] = str(value + 1) # Increases the value by 1 and converts it back to string and updates it

def decrease(): # Event handler function to decrease the value

    value = int(lbl_value["text"])

    lbl_value["text"] = str(value - 1) # Decreases the value by 1 and converts it back to string and updates it

window = tk.Tk() # .Tk class creates a root window

window.rowconfigure(0, minsize=50, weight=1)  # configures the row when expanded and minimum size is 50 pixel

window.columnconfigure([0, 1, 2], minsize=50, weight=1) # configures the three columns when expanded and minimum size is 50 pixel

btn_decrease = tk.Button(master=window, text="-", command=decrease) # assigns window as parent container
# and command attribute calls the increase function when button is tapped

lbl_value = tk.Label(master=window, text="0")

btn_increase = tk.Button(master=window, text="+", command=increase)

btn_decrease.grid(row=0, column=0, sticky="nsew") # Creates a grid and uses sticky parameter to expand on both sides when resized

lbl_value.grid(row=0, column=1)

btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop() # .mainloop() runs the gui