#!/usr/bin/env python3
'''
checkbutton_sample.py
for course material at www.jasaplus.com
'''
from tkinter import Tk, Checkbutton, IntVar, BooleanVar
window = Tk()
window.title("Checkbutton sample")
window.geometry("600x400+300+10")
var = IntVar()
c1 = Checkbutton(window, text=" Check 1", variable=var)
c1.place(x = 200, y = 100)

c2Val = BooleanVar()
c2Val.set(True)
c2 = Checkbutton(window, text=' Check 2', var=c2Val)
c2.pack()

window.mainloop()
