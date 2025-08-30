# imports tkinter gui
import tkinter as tk
# filedialog is a submodule in Tkinter that provides ready-made dialog windows for opening
# and saving files. askopenfilename method opens a file chooser dialog for selecting an
# existing file and asksaveasfilename method opens a save dialog where we can type a new
# file name or select an existing file to overwrite.
# returns the full path of the file we select as a string.
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    # askopenfilename is a method that opens the file explorer dialog to choose a file
    # filetypes specifies text file and any file can be chosen
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # if the user cancels the file explorer dialog stops the function
    if not filepath:
        return
    # clears the text widgets previous texts
    txt_edit.delete("1.0", tk.END)
    # file handling opens the file in utf-8 encoding it ensures can read text in standard encoding
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        # .read method reads the file stores the texts as string in a var
        text = input_file.read()
        # inserting the texts from the text file in the text widget
        txt_edit.insert(tk.END, text)
    # Changing the window title to show the file location
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    # asksaveasfilename is a method that opens the file explorer dialog to create new or overwrite a file
    # filetypes specifies text file and any file can be chosen
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    # file handling opens the file and writes it
    # utf-8 encoding it ensures can read text in standard encoding
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        # gets the texts from the text widget and stores them in a var
        text = txt_edit.get("1.0", tk.END)
        # writes the texts in a new file or saves it in an existing file
        output_file.write(text)
    # Changing the window title to show the file location
    window.title(f"Simple Text Editor - {filepath}")


# .Tk class creates a root window
window = tk.Tk()


# Sets the title of window
window.title("Simple Text Editor")


# configures the row 0 & column 1 when its expanded and minimum size is 300 pixel
# First column 0 doesn't need to expand
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)


# Creating a frame to contain the buttons with raised or tk.RAISED relief & border-width= 2
frm_buttons = tk.Frame(window, relief= "raised", bd=2)


# Creating the text and button widgets
txt_edit = tk.Text(master= window)
btn_open = tk.Button(master= frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(master= frm_buttons, text="Save As...", command=save_file)


# Creating a 1 row/ 2 column grid, and placing frame & text widget in (0, 0) , (0, 1)
# Used sticky= "ns" so frame can expand vertically and text widget can expand in both ways
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


# Creating another 2 row/ 1 column grid inside frame and used sticky= "ew" so buttons can
# expand horizontally
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


# .mainloop() runs the gui
window.mainloop()