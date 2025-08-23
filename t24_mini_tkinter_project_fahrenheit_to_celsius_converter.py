# imports tkinter gui
import tkinter as tk


# .Tk class creates a root window
window = tk.Tk()

# Created a function to the load the converted value in the `C entry widget
def lbl_text(value):
    # Inserting the value in the 0th index
    entry_c.insert(0,value)


# Created a function to get the input from the widget & convert it
def ftoc():
    temp_f = int(entry.get()) # Gets the input
    temp_c = (temp_f - 32) * (5/9) # converts it
    lbl_text(temp_c) # passes the value in other function as parameter


# Creating a list to store the frames
frmList = []


# Creating a nested loop where i iterates 1 time and j iterates 4 times
for i in range(1):
    for j in range(5):
        #Creating a frame for each iteration of j, in total four frames created
        frame = tk.Frame(master=window,relief= tk.RIDGE, borderwidth=1)
        # Creating a 1 row/4 column grid and placing the frames in 0,0/0,1/0,2/0,3 cells
        frame.grid(row=i, column=j)
        # Adding each frames individually in the list
        frmList.append(frame)


# Creating an entry widget to take the input from user
entry = tk.Entry(
    # master= means this widgets parent container is frmList[0] 0th index frame
    master= frmList[0],
    width= 10,
    font= ('Arial', 25),
    borderwidth= 1
)


# Creating a label widget to show the text `F
lbl_f = tk.Label(
    master= frmList[1],
    text= '`F',
    height = 5,
    width = 3
)


# Creating a button widget to tap and start the program
btn_convert = tk.Button(
    master= frmList[2],
    text= '<-->',
    height = 5,
    width = 10,
    command= ftoc
)


entry_c = tk.Entry(
    master= frmList[3],
    width= 10,
    font= ('Arial', 25),
    borderwidth= 1
)


# Creating another label widget to show the output
lbl_c = tk.Label(
    master = frmList[4],
    text = '`C',
    height = 5,
    width = 3
)


# Placing the widgets in the frame to show up
entry.pack()
lbl_f.pack()
btn_convert.pack()
entry_c.pack()
lbl_c.pack()


# .mainloop() runs the gui
window.mainloop()