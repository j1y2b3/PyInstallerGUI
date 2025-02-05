'''用户图形界面'''

import tkinter as tk

import data
from gui.head import Head

class Win:
    '''主窗口'''

    def __init__(self):

        # 初始化窗口
        self.root = tk.Tk()
        self.root.title('PyInstallerGUI')
        self.root.iconbitmap(default=data.getIconPath())
        self.x, self.y = self.root.winfo_screenwidth()//2, self.root.winfo_screenheight()//2
        self.width, self.height = 1000, 600
        self.root.geometry(''.join((f'{self.width}x{self.height}',
                                  f'+{self.x-self.width//2}+{self.y-self.height//2}')))
        self.root.resizable(False,False)

        # 初始化各组件
        self.head = Head(self.root, self.getcommands)

        # 放置各组件
        self.place()

        # 开启主循环
        self.root.mainloop()

        # 退出程序
        self.head.exit()
    
    def getcommands(self) -> tuple:
        '''获取命令'''
        
        return ()
    
    def place(self):
        '''放置各组件'''
        
        self.head.place()