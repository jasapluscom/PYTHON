#!/usr/bin/env python3
'''
popup_sample.py
tkinter sample
for python3 training at jasaplus.com
'''
from tkinter import Tk, Button, messagebox

def OnClick():
    messagebox.showinfo("Information","Info !")
    messagebox.showerror("Error","Error !")
    messagebox.askokcancel("OK CANCEL","Ok or Cancel")

window = Tk()
window.title("Pop up Sample")
window.geometry("600x400+300+50")
window.configure(bg="#00aff0")

btn = Button(window, text="Click Me !", command=OnClick)
btn.place(x = 200, y = 50)

window.mainloop()
