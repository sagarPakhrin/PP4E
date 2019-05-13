from tkinter import *

def greeting():
    print("Hello stdout wrld")

win = Frame()
win.pack()
Button(win, text="Hello",command=greeting).pack(side=LEFT, anchor=N)
Label(win, text="Hello container world").pack(side=TOP)
Button(win, text="Quit",command=win.quit).pack(side=RIGHT)
win.mainloop()
