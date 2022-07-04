import tkinter as tk
window = tk.Tk()

#Constants
window_title = "Placerholder"
window_size = "1000x750"

def draw_window():
    window.geometry(window_size)
    window_title(window_title)
    window.mainloop()