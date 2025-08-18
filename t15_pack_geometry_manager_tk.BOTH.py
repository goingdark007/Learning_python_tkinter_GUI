import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

frame1 = tk.Frame(master=window, width=200, height=100, bg="red") # declares parent container, backgroud color is red
# and at least one frame should have height argument to force the window to have some height

frame2 = tk.Frame(master=window, width=100, bg="yellow")

frame3 = tk.Frame(master=window, width=50, bg="blue")

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # fill=tk.BOTH to make the frames responsive when you resize the window both
# vertically and horizontally,and side=tk.LEFT to stack the frames or widgets at left side.
# Also, expand is used to expand the widget to fill any extra unused space in the parent window

frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop() # .mainloop() runs the gui