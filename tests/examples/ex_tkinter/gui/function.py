import tkinter as tk

import function


class showAdd:
    
    def __init__(self, win):

        self.var_a = tk.IntVar()
        self.var_b = tk.IntVar()
        self.ent_a = tk.Entry(win, textvariable=self.var_a)
        self.ent_b = tk.Entry(win, textvariable=self.var_b)
        self.ent_a.place(x=50, y=50, width=100, height=30)
        self.ent_b.place(x=200, y=50, width=100, height=30)

        self.but = tk.Button(win, text="add", command=self.add)
        self.but.place(x=50, y=100, width=100, height=30)
    
    def add(self):
        
        self.a = self.var_a.get()
        self.b = self.var_b.get()

        function.add(self.a, self.b)


class showSub:

    def __init__(self, win):

        self.var_a = tk.IntVar()
        self.var_b = tk.IntVar()
        self.ent_a = tk.Entry(win, textvariable=self.var_a)
        self.ent_b = tk.Entry(win, textvariable=self.var_b)
        self.ent_a.place(x=350, y=50, width=100, height=30)
        self.ent_b.place(x=500, y=50, width=100, height=30)

        self.but = tk.Button(win, text="sub", command=self.sub)
        self.but.place(x=350, y=100, width=100, height=30)
    
    def sub(self):
        
        self.a = self.var_a.get()
        self.b = self.var_b.get()

        function.sub(self.a, self.b)