import tkinter as tk
import topmenu
window = tk.Tk()

#Constants
window_title = "TkHTML"
window_size = "1000x750"


#Defines and assembles properties of the windows
def draw_window():
    window.geometry(window_size)
    window.title(window_title)
    topmenu.draw_menubar()
    window.mainloop()