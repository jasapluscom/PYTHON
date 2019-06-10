#!/usr/bin/env python3
'''
button_sample.py
for course material at www.jasaplus.com
'''
from tkinter import Tk, Button, messagebox

def OnClick(num):
    messagebox.showinfo("Information","I got clicked at " + str(num))

window = Tk()
window.title("button sample")
window.geometry("600x400+300+10")
btn = Button(window, text="Click Button 1!", command=lambda:OnClick(1))
btn.place(x = 200, y = 50)
btn2 = Button(window, text="Click Button 2 !", command=lambda:OnClick(2))
btn2.place(x = 200, y = 100)
window.mainloop()
