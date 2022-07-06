from tkinter import PhotoImage
import tkinter as tk
import topmenu
window = tk.Tk()

#Constants
window_title = "TkHTML"
window_size = "1000x750"
# https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/ 
# as to why this is here
mainicon = PhotoImage(file = 'tkhtml.png')

#Defines and assembles properties of the windows
def draw_window():
    window.geometry(window_size)
    window.title(window_title)
    window.iconphoto(False, mainicon)
    topmenu.draw_menubar()
    window.mainloop()