#File menu functions
from tkinter import messagebox
from tkinter import filedialog
import tkinter


def save_file():
    save_buffer = text.get(1.0, "end")
    print(save_buffer)
    path = fd.asksaveasfilename()    
    print(path)
    fileout = open(path, 'w')
    fileout.write(save_buffer)
    fileout.close()

def open_file():
    file = fd.askopenfilename()
    filecontent = open(file, "r")
    text.insert(1.0, filecontent.read())

#Edit menu functions
def copy():
    pass

def cut():
    pass

def paste():
    pass

def undo():
    pass

def redo():
    pass

#Help menu functions
def help():
    pass

def about():
    pass

def print_debug():
    print('Hello World! :D')

def box_debug():
    tkinter.messagebox.showinfo(title='Test', message='Hello World! :D')
    
def open_debug():
    singlefile = tkinter.filedialog.askopenfile(mode='r')
    tkinter.messagebox.showinfo(title='File Debug', message=singlefile)

def nested_box():
    tkinter.messagebox.showinfo(title="Nested Menu", message = "Nested Menu Correct!")