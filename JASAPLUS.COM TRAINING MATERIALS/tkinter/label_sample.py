#!/usr/bin/env python3
import tkinter as tk
root = tk.Tk()
root.title("label sample")
root.geometry("600x400+300+10")
w = tk.Label(root, text="Label Sample")
w.pack()
root.mainloop()
