from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class Customui(MyGui):
    def reply(self):
        showinfo(title='popup',message='Ouch!')


if __name__ == "__main__":
    Customui().pack()
    mainloop()
