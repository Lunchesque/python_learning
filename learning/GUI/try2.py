from tkinter import *

class btn:
    def __init__(self):
        self.but = Button(root)
        self.but = Button(root, text = "Print")
        self.but.pack()
        self.but.bind("<Button-1>", self.asd)
        
    def asd(self, event):
        a = int(input('Enter 1st num: '))
        b = int(input('Enter 2nd num: '))
        print(max(a, b))

root = Tk()
obj = btn()
root.mainloop()
