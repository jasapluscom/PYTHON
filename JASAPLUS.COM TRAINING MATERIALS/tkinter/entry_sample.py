#!/usr/bin/env python3
from tkinter import Label, Entry, Tk, mainloop
master = Tk()
master.title("entry sample")
master.geometry("600x400+300+10")
e1 = Entry(master)
e2 = Entry(master)
e1.place(x = 200, y = 50)
e2.place(x = 200, y = 100)
e1.insert(0,"Username")
e2.insert(0,"Password")
mainloop()
