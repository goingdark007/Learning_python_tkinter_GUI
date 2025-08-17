import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

frame1 = tk.Frame(master=window, height=100, bg="red") # declares parent container, backgroud color is red


frame2 = tk.Frame(master=window, height=50, bg="yellow")

frame3 = tk.Frame(master=window, height=25, bg="blue")

frame1.pack(fill=tk.X) #  tk.X to fill in the horizontal direction
# and stack the three frames so that each one fills the whole window horizontally, which can expanded horizontally

frame2.pack(fill=tk.X)

frame3.pack(fill=tk.X)

window.mainloop() # .mainloop() runs the gui