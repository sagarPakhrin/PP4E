from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):

    """Docstring for MyGui. """

    def __init__(self,parent=None):
        """TODO: to be defined1.

        :parent: TODO

        """
        Frame.__init__(self,parent)
        button = Button(self, text='Press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title="popup",message="Button Pressed")


if __name__ == "__main__":
    window = MyGui()
    window.pack()
    window.mainloop()

