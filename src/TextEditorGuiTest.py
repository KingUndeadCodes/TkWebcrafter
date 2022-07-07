from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox

root = Tk()
root.geometry("200x125")
root.title("Micro Notepad")

def save_file():
    save_buffer = text.get(1.0, "end")
    

def open_file():
    file = fd.askopenfilename()
    filecontent = open(file, "r")
    text.insert(1.0, filecontent.read())

def clear():

    text.delete(1.0, "end")

text = Text(root, width = 20, height = 20)
button2 = Button(root, text = "s", command = save_file)
button2.config(height= 1, width = 2, )
button3 = Button(root, text = "o", command = open_file)
button3.config(height= 1, width = 2)
button4 = Button(root, text = "c", command = clear)
button4.config(height= 1, width = 2)
button5 = Button(root)
button5.config(height= 1, width = 2)
button6 = Button(root)
button6.config(height= 1, width = 2)
button7 = Button(root)
button7.config(height= 1, width = 2)

text.pack(expand = True, side = "left")
button2.pack(fill = BOTH, expand = True)
button3.pack(fill = BOTH, expand = True)
button4.pack(fill = BOTH, expand = True)
button5.pack(fill = BOTH, expand = True)

root.mainloop()