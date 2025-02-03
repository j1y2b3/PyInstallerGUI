'''用户图形界面'''

import tkinter as tk
from tkinter import ttk

import data

class Win:

    def __init__(self):
        
        self.win = tk.Tk()
        self.win.title('PyInstallerGUI')
        self.win.iconbitmap(data.get_icon_path())
        self.winx,self.winy = self.win.winfo_screenwidth()//2,self.win.winfo_screenheight()//2
        self.winw,self.winh = 800,600
        self.win.geometry(''.join((f'{self.winw}x{self.winh}',
                                  f'+{self.winx-self.winw//2}+{self.winy-self.winh//2}')))
        self.win.resizable(False,False)

    def run(self):

        self.win.mainloop()
    
    def close(self):

        self.win.destroy()