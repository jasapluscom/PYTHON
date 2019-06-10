#!/usr/bin/env python3
'''
gui3.py
tkinter sample
for python3 training at jasaplus.com
'''
from tkinter import Tk,Canvas, PhotoImage, Label

window = Tk()
window.title("3rd")

window.geometry("600x400+300+10")

C = Canvas(window, bg="white", height=600, width=400)
filename = PhotoImage(file = "images/bg.gif")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

window.mainloop()