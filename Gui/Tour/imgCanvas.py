gifdir = "../gifs/"
from tkinter import *
win = Tk()
img = PhotoImage(file="../gifdir/download.png")
can = Canvas(win,width=2,height=2,image=img,anchor=NW)

can.pack(fill=BOTH)
win.mainloop()
