from tkinter import *
from tkinter2 import MyGui

mainwin = Tk()
Label(mainwin, text=__name__).pack()

popup = Toplevel()
Label(popup,text="Attached").pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
