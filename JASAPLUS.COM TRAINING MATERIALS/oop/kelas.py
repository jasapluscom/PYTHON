#!/usr/bin/env python3
'''
kelas.py
sample class for python3 full stack training
at www.jasaplus.com
'''
class kucing:
    sound = "?"
    habit = "?"

    def __init__(self):
        self.sound = "meow"
        self.habit = "pee"
        #print(type(self))
    def DoHabit(self):
        print("doing " + self.habit)

    def DoSound(self):
        print(self.sound)
