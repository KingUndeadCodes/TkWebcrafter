import tkinter as tk
import topmenu
window = tk.Tk()

#Constants
window_title = "Placerholder"
window_size = "1000x750"
menubar = topmenu.draw_topbar()

def draw_window():
    window.geometry(window_size)
    window.title(window_title)
    topmenu.draw_topbar()
    window.config(menu = menubar)
    window.mainloop()