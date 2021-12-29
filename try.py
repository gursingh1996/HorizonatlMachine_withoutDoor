#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import font
from tkinter.constants import NSEW
import tkinter.ttk as ttk
from typing import Sized

class App(ttk.Frame):

    def __init__(self, parent=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        fram = tk.Frame(self, height=400, width=300, highlightthickness=1, highlightbackground="black")
        fram.grid(row=0, column=0)
        fram.grid_propagate(0)
        for i in range(4):
            fram.rowconfigure(i, weight=1)
            if i < 3:  fram.columnconfigure(i, weight=1)

        
        keypadVal=1
        for i in range(3):
            for j in range(3):
                tk.Button(fram, text=keypadVal, fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=i, column=j, sticky="nsew")
                keypadVal+=1
        tk.Button(fram, text=".", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=0, sticky="nsew")
        tk.Button(fram, text="0", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=1, sticky="nsew")
        tk.Button(fram, text="C", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=2, sticky="nsew")
        


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x300')

    app = App(root)
    app.grid(row=0, column=0, sticky='nsew')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()