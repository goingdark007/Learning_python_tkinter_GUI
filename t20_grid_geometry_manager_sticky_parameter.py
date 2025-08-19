import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

window.columnconfigure(0, minsize=250) # configures the column when expanded and minimum size is 250 pixel

window.rowconfigure([0, 1], minsize=100) # configures the two rows when expanded and minimum size is 100 pixel


label1 = tk.Label(text="A")

label2 = tk.Label(text="B")

label1.grid(row=0, column=0, sticky="ne") # Creates a grid with two rows and one column
# "ne" to place top right corner of the cell and "sw" to place bottom left corner of the cell

label2.grid(row=1, column=0, sticky="sw")

window.mainloop() # .mainloop() runs the gui