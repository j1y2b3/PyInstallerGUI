'''用户图形界面'''

import tkinter as tk

from gui.required import Required
import data

class Win:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title('PyInstallerGUI')
        self.root.iconbitmap(data.get_icon_path())
        self.rootx, self.rooty = self.root.winfo_screenwidth()//2, self.root.winfo_screenheight()//2
        self.rootw, self.rooth = 1000, 600
        self.root.geometry(''.join((f'{self.rootw}x{self.rooth}',
                                  f'+{self.rootx-self.rootw//2}+{self.rooty-self.rooth//2}')))
        self.root.resizable(False,False)
    
    def show(self):
        '''显示内容'''

        self.required = Required(self.root)

        self.required.place()

    def loop(self):
        '''进入循环'''

        self.root.mainloop()
    
    def close(self):
        '''关闭窗口'''

        self.root.destroy()