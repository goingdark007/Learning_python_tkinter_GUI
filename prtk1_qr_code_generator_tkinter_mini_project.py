import qrcode  # imports qrcode library
import tkinter as tk  # imports tkinter as Tk()
from tkinter import filedialog  # imports filedialog submodule for file saving
import os  # imports system
from PIL import ImageTk  # Pillow library allows tkinter to display png and jgp files

# Declaring a variable to store the qr code image and use it in multiple functions
qr_img = None


# This Function is responsible to take the input convert it to qr code show it in the window
def get_qr_code():
    # Gets the data from the textvariable using .get() method and strip method is used to
    # remove any unwanted spaces before the text
    data_var = data.get().strip()

    # Checks if the input field is empty.If its empty it will stop the function and show error
    if data_var == "":
        # config updates the label with the error msg in the run time also changes foreground color
        lbl_data.config(text="⚠ Please fill all fields", fg="red")
        return

    # Used global keyword to use the global variable qr_image locally in a function
    global qr_img
    # qrcode.make() methods generates QR code as a PIL (png, jpeg) image and saves it in a variable
    qr_img = qrcode.make(data_var)
    # Calls the show_qr function to show the updated qr code in a new window
    show_qr()
    lbl_data.config(text="✅ QR code generated successfully", fg="green")


# This function creates a new window and displays the qr code image
def show_qr():
    """Create a new window and display the QR code"""
    global qr_img
    # Toplevel() creates another new window which is the child of our root window
    top = tk.Toplevel(master=window)
    # Sets the title of the new window
    top.title("Your QR Code")
    # Sets the size of the new window
    top.geometry("300x300")
    # Prevents the window from being resized
    top.resizable(False, False)
    # Image.TkPhotImage() converts PIL image to Tkinter Image
    qr_tk: ImageTk.PhotoImage = ImageTk.PhotoImage(qr_img)
    # Put into a Label widget
    # image=qr_tk will show image in the label instead of showing text
    # noinspection PyTypeChecker
    label = tk.Label(top, image=qr_tk)
    # we must keep a reference to the image object (qr_tk) in the code.
    # If we don’t, Python’s garbage collector deletes it, and the label will appear blank
    label.image = qr_tk
    # places the widget in the window
    label.pack(padx=20, pady=20)


# This function saves the generated qr code image to the user specified location
def save_code():
    global qr_img

    # if no qr code is generated it will stop the function and update the label to show error msg
    if qr_img is None:
        # config updates the label with the error msg in the run time also changes foreground color
        lbl_save.config(text="⚠ Please generate QR code first", fg="red")
        return

    # Gets the file name from the textvariable of the entry widget
    save_data = name_to_save.get()

    # if file name is not entered it will stop the function and show error
    if not save_data:
        lbl_save.config(text="⚠ Please fill all fields", fg="red")
        return

    # .askdirectory() is a method that opens a directory selection dialog window which returns the selected directory
    # path as a string. title parameter sets the dialog window's title to "Select Save Location"
    save_dir = filedialog.askdirectory(title="Select Save Location")
    # if no directory/path is selected it will stop the function and show error
    if save_dir:
        # os.path.join() creates a complete file path by joining the selected directory path (save_dir) with a filename
        # created from save_data with .png extension. Basically string concatenation but more smartly for cross-platform
        filepath = os.path.join(save_dir, f"{save_data}.png")
        # PIL's qr_img.save() method saves the QR code image (qr_img) to the constructed filepath
        # The image is saved in PNG format as specified in the filepath
        qr_img.save(filepath)
        lbl_save.config(text=f"✅ Saved at {filepath}", fg="green")


# .Tk class creates a root window
window = tk.Tk()
# .geometry(width*height) method used to set the initial size of our window.
window.geometry("600x400")
# Sets the name / title of the window
window.title("QR Code Generator")
# Prevents the window from being resized
window.resizable(False, False)

# Variables to store user input
data = tk.StringVar()  # Stores String value
name_to_save = tk.StringVar()

# label widget to show field name and entry widget for file name input
lbl_save = tk.Label(master=window, text="SAVE_AS")
lbl_save.place(x=160, y=100)
etr_save = tk.Entry(master=window, textvariable=name_to_save, width=25, font=("Arial", 15))
etr_save.place(x=160, y=125)

# label widget to show field name and entry widget for data input
lbl_data = tk.Label(master=window, text="INSIDE QRCODE")
lbl_data.place(x=160, y=155)
etr_data = tk.Entry(master=window, textvariable=data, width=25, font=("Arial", 15))
etr_data.place(x=160, y=175)

# Button to generate QR code
btn_code = tk.Button(master=window, text="Get Code", command=get_qr_code, width=30, height=2, bg="grey")
btn_code.place(x=192, y=220)

# Button to save generated QR code
btn_save = tk.Button(master=window, text="Save as", command=save_code, width=30, height=2, bg="grey")
btn_save.place(x=192, y=260)

# .mainloop() runs the gui
window.mainloop()