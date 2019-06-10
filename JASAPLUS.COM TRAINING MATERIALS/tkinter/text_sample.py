#!/usr/bin/env python3
'''
text_sample.py
for course material at www.jasaplus.com
'''
from tkinter import Tk, Text, END

window = Tk()
window.title("text sample")
window.geometry("600x400+300+10")

Teks = Text(window, height=2, width=30)
Teks.pack()
Teks.insert(END, "first line\ntwo line\n")

Teks2 = Text(window, height=5, width=40)
Teks2.insert(END, "first line\ntwo line\n")
Teks2.place(x = 200, y = 100)

window.mainloop()
