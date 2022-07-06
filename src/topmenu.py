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
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = windowMain.window.quit)

    def edit_submenu():
        edit_menu = Menu(menu_bar)
        menu_bar.add_cascade(label = "Edit", menu = edit_menu)
        edit_menu.add_command(label = "Copy", command = copy)
        edit_menu.add_command(label = "Cut", command = cut)
        edit_menu.add_command(label = "Paste", command = paste)
        edit_menu.add_separator()
        edit_menu.add_command(label = "Undo", command = undo)
        edit_menu.add_command(label = "Redo", command = redo)

    def help_submenu():
        help_menu = Menu(menu_bar)
        menu_bar.add_cascade(label = "Help", menu = help_menu)
        help_menu.add_command(label = "Help", command = help)
        help_menu.add_command(label = "About", command = about)

    #Assemble submenu functions to draw the menu bar
    file_submenu()
    edit_submenu()
    help_submenu()
    windowMain.window.config(menu = menu_bar)
