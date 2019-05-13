import sys
from tkinter import *

class HelloCallable:
    def __init__(self):
        self.msg='Hello __call__ world'


    def __call__(self):
        print(self.msg)
        sys.exit()

widget = Button(None, text="hello event world", command=HelloCallable())
widget.pack()
widget.mainloop()
