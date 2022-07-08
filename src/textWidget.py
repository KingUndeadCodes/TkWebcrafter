#This file will make the Text widget and the edit buttons.
from tkinter import Text
import windowMain

def draw_text():
    textbox = Text(windowMain.window)
    textbox.pack(anchor = "w")
