#!/usr/bin/env python3
'''
menubutton_sample.py
for course material at www.jasaplus.com
'''
from tkinter import Tk, Menubutton, Menu, RAISED

def page(container):
    print("Page selected: " + container)

window = Tk()
window.title("Menubutton sample")
window.geometry("600x400+300+10")
window.configure(bg="#00aff0")
mbutton = Menubutton(window, text="Menu")
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='Home', command=lambda:page("home"))
picks.add_command(label='About', command=lambda:page("about"))
picks.add_command(label='Contact', command=lambda:page("contact"))
mbutton.place(x = 10, y = 20)
mbutton.config(bg='#ffffff', bd=1, relief=RAISED)
window.mainloop()
