from tkinter import *
from tkinter.colorchooser import askcolor
from quitter import Quitter 

def setBgColor():
    (tripple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)

root = Tk()
push = Button(root,text='Set background color',command=setBgColor)
push.config(height=3, font=('times',20,'bold'))
push.pack(expand=YES, fill=BOTH)
quitter = Quitter()
root.mainloop()
