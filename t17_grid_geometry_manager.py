import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

for i in range(3): # nested loop for taking i as row number and j as column number

    for j in range(3):

        frame = tk.Frame(

            master=window, # declares parent container

            relief=tk.RAISED, # gives the frame a border that makes it appear to stick out from the screen.

            borderwidth=1 # sets the border width to 1
        )

        frame.grid(row=i, column=j) # Creates the grid iteratively according to i and j

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}") # Creates a label widget which is contained by frame

        label.pack() # to place the widget in the window

window.mainloop() # .mainloop() runs the gui