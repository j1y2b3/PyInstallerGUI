'''打包参数选择
name
icon
console
filestyle
distpath
workpath
specpath
coverdist
coverwork
loglevel              # TRACE DEBUG INFO WARN ERROR CRITICAL
data                  # [(编译时文件位置, 运行时文件位置), ...]
binary                # 同上
moreimportpaths       # 额外导入的包
morehiddenimports     # 额外隐藏导入的包
excludemodules        # 排除的包
runtimetmpdir         # 运行时临时目录，用于onefile且有data或binary时
'''

import tkinter as tk
from tkinter import ttk

from gui.details import __all__ as arguments


class Option:
    '''单个参数部件'''

    def __init__(self, root, text):
             
        self.root = root

        self.var = [tk.BooleanVar(), tk.StringVar()]
        self.chkbut = ttk.Checkbutton(self.root,
                                      variable=self.var[0])
        self.radbut = ttk.Radiobutton(self.root,
                                      text=text,
                                      variable=self.var[1],
                                      value=text,
                                      style='TButton')
    
    def place(self, x, y):
        '''放置各组件'''

        self.chkbut.place(x=x, y=y+2)
        self.radbut.place(x=x+20, y=y, width=200, height=30)


class Optional():
    '''打包参数选择'''

    def __init__(self,root):

        self.root = root
        self.frame = ttk.Frame(self.root,
                               relief='solid')
        self.options = {}

        # 确认命令
        self.but_ok = ttk.Button(self.frame,
                                 text='确认命令',
                                 command=self.getCommands)

        # 各参数
        style = ttk.Style()
        style.configure('TButton')

        for arg in arguments:
            self.options[arg] = Option(self.frame, arg)
    
    def getCommands(self):
        '''获取打包命令'''

        pass
    
    def place(self):
        '''放置各组件'''

        self.frame.place(x=0, y=90, width=300, height=660)

        self.but_ok.place(x=20, y=10, width=250, height=30)

        x, y = 30, 10
        dy = 40
        '''要做滚动条
        for arg in arguments:
            y += dy
            self.options[arg].place(x=x, y=y)'''
        y += dy
        self.options['name'].place(x=x, y=y)
        y += dy*10
        print(y)
        self.options['icon'].place(x=x, y=y)
    

    