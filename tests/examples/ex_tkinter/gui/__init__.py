import os
import tkinter as tk

from gui import function
import data

class Win:

    def __init__(self):

        self.win=tk.Tk()
        self.win.title('example1')
        self.win.geometry('700x300')
        self.win.resizable(False,False)
        self.win.iconbitmap(default=data.get_icon_path())

        function.showAdd(self.win)
        function.showSub(self.win)

        self.win.mainloop()