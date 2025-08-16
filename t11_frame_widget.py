import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

frame_a = tk.Frame() # Creates a frame widget. Frames are like containers for other widgets.

frame_b = tk.Frame() # A widget can be assigned to a frame by setting the widget’s master attribute

label_a = tk.Label(master=frame_a, text="I'm in Frame A") # frame_a contains a label with the text "I'm in Frame A"


label_b = tk.Label(master=frame_b, text="I'm in Frame B") # frame_b contains the label "I'm in Frame B"


label_a.pack() # to place the widget in the window.

label_b.pack()

frame_a.pack() # By swapping a and b the order is changed too

frame_b.pack()

window.mainloop() # .mainloop() runs the gui