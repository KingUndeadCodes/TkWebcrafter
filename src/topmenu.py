from tkinter import *
import windowMain

#Special thanks to Blue Badger from Grepper :)
def draw_filemenu():
    file_menubar = Menu(windowMain.window)
    filemenu = Menu(file_menubar, tearoff=0)
    filemenu.add_command(label="New - Ctrl + N")
    filemenu.add_command(label="Open - Ctrl + O")
    filemenu.add_command(label="Save - Ctrl + S")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=windowMain.window.quit)
    file_menubar.add_cascade(label="File", menu=filemenu)
    windowMain.window.config(menu=file_menubar)
    return file_menubar

# def draw_helpmenu():
#     menubar = Menu(windowMain.window)
#     helpmenu = Menu(menubar, tearoff=0)
#     helpmenu.add_command(label="About")
#     helpmenu.add_command(label="Help - F1")
#     helpmenu.add_command(label="Keyboard Shortcuts - Ctrl + K")
#     menubar.add_cascade(label="Help", menu=helpmenu)

def draw_topbar():
    draw_filemenu()
    # draw_helpmenu()