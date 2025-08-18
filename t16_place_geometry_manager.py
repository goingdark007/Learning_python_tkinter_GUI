import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

frame = tk.Frame(master=window, width=150, height=150)  # declares parent container, and sets width and height to 150 pixels

frame.pack() # to place the frame in the window.

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red") # the label is contained by the frame, bg is red

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow") # bg is yellow

label1.place(x=0, y=0) # to  place it in frame at position (0, 0)

label2.place(x=75, y=75) # to  place it in frame at position (75, 75)

window.mainloop() # .mainloop() runs the gui