from tkinter import *
from menubarFunctions import *
import windowMain


def draw_menubar():
    menu_bar = Menu(windowMain.window)

    def file_submenu():
        file_menu = Menu(menu_bar)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "Save", command = save_file)
        file_menu.add_command(label = "Open", command = open_file)
        file_menu.add_command(label = "Exit", command = windowMain.window.quit)

    file_submenu()
    windowMain.window.config(menu = menu_bar)
