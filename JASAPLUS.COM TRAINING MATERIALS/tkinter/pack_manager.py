#!/usr/bin/env python3
'''
pack_manager.py
tkinter pack manager sample
for python3 training at www.jasaplus.com
'''

from tkinter import Tk,Button, Frame, LEFT, RIGHT, BOTTOM, TOP, RAISED, X, Y, BOTH

master = Tk()
master.title("Pack Manager")
master.geometry("600x400+300+10")

frame1 = Frame(master, relief=RAISED, borderwidth=1, bg='#3b6a12',height='200')
frame1.pack(fill=X)

#side option
btn1 = Button(frame1, text="Button 1")
btn1.pack(side=LEFT)

btn2 = Button(frame1, text="Button 2")
btn2.pack(side=RIGHT)

btn3 = Button(frame1, text="Button 3")
btn3.pack(side=TOP)

btn4 = Button(frame1, text="Button 4")
btn4.pack(side=BOTTOM)

frame2 = Frame(master, relief=RAISED, borderwidth=1, bg='#8bde41',height='200')
frame2.pack(fill=X)

#fill option
btn1x = Button(frame2, text="Button 1")
btn1x.pack(fill=X)

btn1x = Button(frame2, text="Button 1")
btn1x.pack(fill=None)

master.mainloop()
