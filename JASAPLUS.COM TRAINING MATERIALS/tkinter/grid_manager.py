#!/usr/bin/env python3
'''
grid_manager.py
tkinter grid manager sample
for python3 training at www.jasaplus.com
'''

from tkinter import Tk,Button

master = Tk()
master.title("Grid Manager")
master.geometry("600x400+300+10")

btn1 = Button(master, text="Button 1")
btn1.grid(row=1, column=1)

btn2 = Button(master, text="Button 2")
btn2.grid(row=1, column=2)

btn3 = Button(master, text="Button 3")
btn3.grid(row=1, column=3)

btn4 = Button(master, text="Button 4")
btn4.grid(row=2, column=1)

btn5 = Button(master, text="Button 5")
btn5.grid(row=2, column=2)

btn6 = Button(master, text="Button 6")
btn6.grid(row=2, column=3)

master.mainloop()
