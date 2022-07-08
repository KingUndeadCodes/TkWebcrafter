#This file will make the Text widget and the edit buttons.
import tkinter
import tkinter.font as tkfont
import windowMain

#Make tab size and font configurable in settings.json
tab_size = 4
user_font = "consolas"

def draw_text():
    textbox = tkinter.Text(windowMain.window)
    textbox_font = tkfont.Font(font = textbox['font'])
    tab = textbox_font.measure(' ' * tab_size)
    textbox.config(height = 45, font = user_font, tabs = tab)
    textbox.pack(
        anchor = "w",
        padx = 15,
        expand = "true", 
        )
