# imports tkinter gui
import tkinter as tk


# .Tk class creates a root window
window = tk.Tk()


# configures the row & column when  its expanded and minimum size is 50 pixel
window.rowconfigure(0, weight= 1, minsize= 50)
window.columnconfigure([0, 1, 2], weight= 1, minsize = 50)


# Global variable to remember which entry was last typed in
last_edited = None


#This function runs whenever a key is pressed inside an Entry. It stores the entry widget
# (entry or entry_c) in last_edited
def set_last_edited(event):
    # global means modifying the global var not creating a local one for function
    global last_edited
    # event.widget tells us which widget triggered the event (either entry or entry_c)
    last_edited = event.widget


def convert():

    global last_edited
    # Checks the last edited field and converts it. If Fahrenheit was last edited it will
    # match with the entry widget of fahrenheit
    if last_edited == entry:
        # gets the input of entry widget as string
        f_val = entry.get()
        # if there is a value it will run the code
        if f_val:
            # Error handling if letter is typed instead of numbers
            try:
                # float() converts the string to decimal number
                temp_c = (float(f_val) - 32) * 5 / 9
                # clears the entry widgets previous texts
                entry_c.delete(0, tk.END)
                # inserts the new value or updated value in the widget
                entry_c.insert(0, f"{temp_c:.2f}") # using f string :.2f takes two decimal value
            # if string is entered then ValueError happens and this code runs
            except ValueError:
                entry_c.delete(0, tk.END)
                # Clears previous text in the entry widget and inserts Error
                entry_c.insert(0, "Error")

    #  if Celsius was last edited it will match with the entry widget of celsius
    elif last_edited == entry_c:
        c_val = entry_c.get()
        if c_val:
            try:
                temp_f = (float(c_val) * 9 / 5) + 32
                entry.delete(0, tk.END)
                entry.insert(0, f"{temp_f:.2f}")
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "Error")


# Creating a list to store the frames
frmList = []


# Creating a nested loop where i iterates 1 time and j iterates 3 times
for i in range(1):
    for j in range(3):
        #Creating a frame for each iteration of j, in total four frames created
        frame = tk.Frame(master=window,relief= "ridge", borderwidth=1)
        # Creating a 1 row/3 column grid and placing the frames in 0,0/0,1/0,2 cells
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
    master= frmList[0],
    text= '`F',
    height = 5,
    width = 3
)


# Creating a button widget to tap and start the program
btn_convert = tk.Button(
    master= frmList[1],
    text= '<-->',
    height = 4,
    width = 10,
    command= convert
)


entry_c = tk.Entry(
    master= frmList[2],
    width= 10,
    font= ('Arial', 25),
    borderwidth= 1
)


# Creating another label widget to show the output
lbl_c = tk.Label(
    master = frmList[2],
    text = '`C',
    height = 5,
    width = 3
)


# Binds the widgets to event function. <Key> = keyboard sensor: goes off whenever we type
# something inside the widget and <FocusIn> = attention sensor: goes off when the widget
# gains the user’s focus (clicked or tabbed into) & lastly it calls the event function which updates the last_edited
entry.bind("<Key>", set_last_edited)
entry_c.bind("<Key>", set_last_edited)
entry.bind("<FocusIn>", set_last_edited)
entry_c.bind("<FocusIn>", set_last_edited)


# Placing the widgets in the frame to show up
# side= tk.LEFT / "left" parameter is used to stack widgets in a frame at the left side by default it stacks at top
entry.pack(side= "left")
lbl_f.pack()
# padx= and pady= to give a lil bit of space between button widget and frame border both horizontally & vertically
btn_convert.pack(padx= 5, pady= 5)
entry_c.pack(side= 'left')
lbl_c.pack()


# .mainloop() runs the gui
window.mainloop()