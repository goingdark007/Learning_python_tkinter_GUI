import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

window.rowconfigure(0, weight= 1, minsize=50) # configures the row when expanded and minimum size is 50 pixel

window.columnconfigure([0, 1, 2, 3], weight= 1, minsize=50) # configures the four columns when expanded and minimum size is 50 pixel

label1 = tk.Label(text="1", bg="black", fg="white") # Creates four label widgets to place in grid

label2 = tk.Label(text="2", bg="black", fg="white")

label3 = tk.Label(text="3", bg="black", fg="white")

label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0) # creates a 1 row and 4 column grid and places it in the first cell

label2.grid(row=0, column=1, sticky="ew") # ns is like pack geometries fill=tk.Y

label3.grid(row=0, column=2, sticky="ns") # ew is like pack geometries fill=tk.X

label4.grid(row=0, column=3, sticky="nsew") # nsew is like pack geometries fill= tk.BOTH

window.mainloop() # .mainloop() runs the gui