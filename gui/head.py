'''窗口顶部部件
选择Python文件
查看命令
确认打包
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import data

class Head:
    '''窗口顶部部件'''

    def __init__(self, root: tk.Tk, getcommandsfunction: callable):

        self.root = root
        self.getCommands = getcommandsfunction
        self.frame = ttk.Frame(self.root)
        self.maxrecentfiles = 8
        self.nonrecentfiles = '最近没有打开Python文件'
        self.recentfiles = self.getRecentFiles()

        # 选择Python文件
        self.but_select = ttk.Button(self.frame,
                                     text='选择Python文件',
                                     command=self.selectPythonFile)
        self.cbox_pythonfile = ttk.Combobox(self.frame,
                                           values=self.recentfiles)
        self.cbox_pythonfile.bind('<<ComboboxSelected>>', self.addRecentFile)

        # 查看命令
        self.text_commands = tk.Text(self.frame)
        self.text_commands.insert('end', '打包命令：\n')
        self.text_commands.config(state='disabled')

        # 确认打包
        self.but_confirm = ttk.Button(self.frame,
                                      text='确认打包',
                                      command=self.makePackage)
    
        # 运行程序
        self.but_run = ttk.Button(self.frame,
                                  text='运行程序',
                                  command=self.runProgram)
    
    # 选择Python文件
    def selectPythonFile(self):
        '''选择Python文件'''

        newfile = filedialog.askopenfilename(filetypes=[('Python File', '*.py;*.pyw')])
        self.cbox_pythonfile.set(newfile)
        self.addRecentFile()
    
    def addRecentFile(self, event=None):
        '''添加最近打开的文件'''

        # 添加
        newfile = self.cbox_pythonfile.get()
        if newfile == self.nonrecentfiles:
            self.cbox_pythonfile.set('')
            return
        if newfile in self.recentfiles:
            self.recentfiles.remove(newfile)
        if newfile:
            self.recentfiles.append(newfile)


        # 更新
        if self.nonrecentfiles in self.recentfiles:
            self.recentfiles.remove(self.nonrecentfiles)
        
        self.recentfiles = self.recentfiles[-self.maxrecentfiles:]
        self.cbox_pythonfile.config(values=self.recentfiles)

    def getRecentFiles(self) -> list[str]:
        '''获取最近打开的Python文件路径'''

        self.recentfiles = data.getRecentFiles()

        if self.recentfiles:
            return self.recentfiles
        else:
            return [self.nonrecentfiles]

    def writeRecentFiles(self):
        '''写入最近打开的Python文件路径'''

        data.writeRecentFiles(self.recentfiles)
    
    # 确认打包
    def makePackage(self):
        '''确认打包'''

        pass
    
    # 运行程序
    def runProgram(self):
        '''试运行打包好的程序'''

        pass
    
    def place(self):
        '''放置各组件'''

        self.frame.place(x=0, y=0, width=1000, height=150)

        self.but_select.place(x=10, y=10, width=300, height=30)
        self.cbox_pythonfile.place(x=10, y=40, width=300, height=30)

        self.text_commands.place(x=630, y=10, width=350, height=60)

        self.but_run.place(x=320, y=40, width=300, height=30)

        self.but_confirm.place(x=320, y=10, width=300, height=30)
    
    def exit(self):
        '''退出程序'''

        self.writeRecentFiles()

                                     