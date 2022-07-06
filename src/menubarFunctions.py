#File menu functions
from tkinter import messagebox
from tkinter import filedialog
import tkinter


def save_file():
    pass

def open_file():
    pass

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