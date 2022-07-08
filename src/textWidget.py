#This file will make the Text widget and the edit buttons.
import tkinter
import windowMain

def draw_text():
    textbox = tkinter.Text(windowMain.window)
    textbox.pack(
        anchor = "w",
        padx = 15,
        expand = "true", 
        )
