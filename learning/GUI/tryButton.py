from tkinter import *

root = Tk()

but = Button(root, text = "This is a btn", width = 30, height = 5, bg = "white", fg = "blue")
lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
but.pack()
root.mainloop()
