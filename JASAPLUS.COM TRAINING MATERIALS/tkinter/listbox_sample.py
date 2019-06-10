#!/usr/bin/env python3
'''
_sample.py
for course material at www.jasaplus.com
'''
from tkinter import Tk, Listbox, END

window = Tk()
window.title("button sample")
window.geometry("600x400+300+10")

listbox = Listbox(window)
listbox.place(x = 200, y = 50)
listbox.insert(END, "select menu")

for item in ["cheese", "burger", "ice cream"]:
    listbox.insert(END, item)

window.mainloop()
