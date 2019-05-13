import sys
from tkinter import *
widget = Button(None, text="Hello world", command = sys.exit)
widget.pack(side=TOP)
widget.mainloop()
