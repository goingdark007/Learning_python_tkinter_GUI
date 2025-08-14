import tkinter as tk # imports tkinter gui

window = tk.Tk() # .Tk class creates a root window

greetings = tk.Label(text ='Hello, Tkinter') # Label is a widget that displays static text or image

greetings.pack() # to place the widget in the window. Pack stacks widget left to right or top to bottom
# There is .grid() to place widgets in row/column table and .place() using exact coordinates

window.mainloop() # .mainloop() runs the gui