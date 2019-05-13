import sys
from tkinter import *

win1 = Toplevel()
win2 = Toplevel()
Button(win1, text='Spam', command=sys.exit).pack()
Button(win2, text="Spam", command=sys.exit).pack()

Label(text="Popus").pack()
win1.mainloop()
