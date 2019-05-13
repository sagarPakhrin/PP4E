from tkinter import *
root = Tk()
Button(root, text="Press", command=root.quit).pack(side=LEFT)
# To aloocate all available space to the button but not stretch
# Button(root,text='Press',command=root.quit).pack(side=LEFT, expand=YES)
# Button(root,text='Press',command=root.quit).pack(side=LEFT, expand=YES, fill=X)
root.mainloop()
