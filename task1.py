#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
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
            lb = tk.Label(text=sys.argv[3:], font=('Courier', '22'))
        else:
            lb = tk.Label(text=sys.argv[1:sys.argv.index("-t")], font=('Courier', '22'))
    else:
        raise ValueError("Должно быть задано число после аргумента -t")
else:
    root.after(5000, kill)
    lb = tk.Label(text=sys.argv[1:], font=('Courier', '22'))

lb.pack()
root.mainloop()
print(sys.argv)
