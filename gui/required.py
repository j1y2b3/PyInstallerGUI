'''必填项
pythonfile: *.py; *.pyw
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Required:

    def __init__(self, win: tk.Tk,
                 *, butopts: dict = {}, entopts: dict = {}, **options):

        self.win = win

        self.frame = ttk.Frame(self.win, **options)

        self.but_pythonfile = ttk.Button(self.frame,
                                         text='选择Python文件',
                                         command=self.selectPythonFile,
                                         **butopts)
        self.pythonfile_var = tk.StringVar()
        self.ent_pythonfile = ttk.Entry(self.frame,
                                        textvariable=self.pythonfile_var,
                                        **entopts)
    
    def selectPythonFile(self):
        '''选择python文件'''

        pythonfile = filedialog.askopenfilename(filetypes=[('Python File', '*.py;*.pyw')])
        self.pythonfile_var.set(pythonfile)
    
    def place(self, **sites):
        '''放置并显示内容'''

        if sites:
            self.frame.place(**sites)
        else:
            self.frame.place(x=0, y=0, width=450, height=100)
        self.but_pythonfile.place(x=10, y=10, width=430, height=30)
        self.ent_pythonfile.place(x=10, y=40, width=430, height=30)
    
    def get(self) -> str:
        '''获取python文件路径'''

        return self.pythonfile_var.get()
