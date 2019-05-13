import sys
from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Verify','Do you really want to quit?'):
        showwarning('Yes',sys.exit())
    else:
        showinfo('No', 'Quit has been canceled')

errmsg = 'Sorry, no spam allowed'
Button(text='Quit',command=callback).pack(fill=X)
Button(text='Spam',command=(lambda:showerror('Spam',errmsg))).pack(fill=X)
mainloop()
