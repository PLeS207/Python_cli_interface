#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox as mb
import sys


def kill():

    root.destroy()


root = tk.Tk()
if "-t" in sys.argv:
    #Проверка на дурака
    if sys.argv[sys.argv.index("-t") + 1].isdigit():
        root.after(sys.argv[sys.argv.index("-t") + 1], kill)
        #Проверка позиционного аргумента
        if sys.argv.index("-t") == 1:
            mb.showinfo(title='Это сообщение', message=sys.argv[3:])
        else:
            mb.showinfo(title='Это сообщение', message=sys.argv[1:sys.argv.index("-t")])
    else:
        raise ValueError("Должно быть задано число после аргумента -t")
else:
    root.after(5000, kill)
    mb.showinfo(title='Это сообщение', message=sys.argv[1:])
root.mainloop()
