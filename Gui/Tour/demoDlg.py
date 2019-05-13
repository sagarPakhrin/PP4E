"""Create a bar of simple buttons that launches dialog demos"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        Label(self,text="Basic Demos").pack()
        for(key,value) in demos.items():
            func = (lambda key=key:self.printit(key))
            Button(self,text=key,command=func).pack(side=TOP,fill=BOTH)
        Quitter(self).pack(side=TOP,fill=BOTH)

    def printit(self,name):
        print(name, 'returns =>',demos[name]())

if __name__ == "__main__":
    Demo().mainloop()
