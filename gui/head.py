'''窗口顶部部件
选择Python文件
查看命令
确认打包
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Head:
    '''窗口顶部部件'''

    def __init__(self, root: tk.Tk, getcommandsfunction: callable):

        self.root = root
        self.getCommands = getcommandsfunction
        self.frame = ttk.Frame(self.root)

        # 选择Python文件
        self.but_select = ttk.Button(self.frame,
                                     text='选择Python文件',
                                     command=self.selectPythonFile)
        self.cbox_pthonfile = ttk.Combobox(self.frame,
                                           values=self.getRecentPythonFiles())

        # 查看命令
        self.but_view = ttk.Button(self.frame,
                                   text='查看命令',
                                   command=self.viewCommands)
        self.text_commands = tk.Text(self.frame,
                                     wrap='word')

        # 确认打包
        self.but_confirm = ttk.Button(self.frame,
                                      text='确认打包',
                                      command=self.makePackage)
    
    def selectPythonFile(self):
        '''选择Python文件'''

        pythonfile = filedialog.askopenfilename(filetypes=[('Python File', '*.py;*.pyw')])
        self.cbox_pthonfile.set(pythonfile)
    
    def viewCommands(self):
        '''查看命令'''

        pass
    
    def makePackage(self):
        '''确认打包'''

        pass

    def getRecentPythonFiles(self) -> tuple[str]:
        '''获取最近打开的Python文件'''

        return ()
    
    def place(self):
        '''放置各组件'''
        
        self.frame.pack(side='top', fill='x')
        self.but_select.grid(row=0, column=0, padx=5, pady=5)
        self.cbox_pthonfile.grid(row=0, column=1, padx=5, pady=5)
        self.but_view.grid(row=0, column=2, padx=5, pady=5)
        self.text_commands.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

                                     