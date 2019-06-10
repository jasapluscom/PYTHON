#!/usr/bin/env python3
'''
place_manager.py
tkinter place manager sample
for python3 training at www.jasaplus.com
'''

from tkinter import Tk,Button

master = Tk()
master.title("Place Manager")
master.geometry("600x400+300+10")

btn1 = Button(master, text="Button 1")
btn1.place(x=1, y=200)

btn2 = Button(master, text="Button 2")
btn2.place(x=100, y=200)

btn3 = Button(master, text="Button 3")
btn3.place(x=200, y=200)

master.mainloop()
