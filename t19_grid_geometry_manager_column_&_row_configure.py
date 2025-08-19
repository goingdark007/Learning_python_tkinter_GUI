import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

for i in range(3): # nested loop for taking i as row number and j as column number

    window.columnconfigure(i, weight= 1, minsize= 75) # it controls how space is allocated in a grid
    # the index of the row/column that needs to be configured
    # weight decides how much a row/column should expand proportionally when the window resizes.
    # minsize sets a minimum size so things don’t collapse when too small

    window.rowconfigure(i, weight= 1, minsize= 50)

    for j in range(3):

        frame = tk.Frame(

            master=window, # declares parent container

            relief=tk.RAISED, # gives the frame a border that makes it appear to stick out from the screen.

            borderwidth=1 # sets the border width to 1
        )

        frame.grid(row=i, column=j, padx= 5, pady=5) # Creates the grid iteratively according to i and j
        # padx and pady adds 5 pixel padding both horizontally and vertically

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}") # Creates a label widget which is contained by frame

        label.pack(padx= 5, pady= 5) # to place the widget in the window and give a lil bit of space between label widget and frame border

window.mainloop() # .mainloop() runs the gui