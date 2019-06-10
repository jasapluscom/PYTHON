#!/usr/bin/env python3

'''
polymorphism sample
created by Antonius Ringlayer
www.jasaplus.com - www.ringlayer.com

oop material for python3 course
'''

class Robot():
    def __init__(self, name):
        self.name = name

    def Steering(self):
        print("[+] By default, my steering is differential drive")

    def Brain(self):
        print("[+] By default, my brain consist of deep learning models")

    def SayMyName(self):
        print("My name is {}".format(self.name))

class WallE(Robot):
    def __init__(self, name):
        self.name = name

    def Steering(self):
        print("[+] {} : By default, my steering is modern skid steering".format(self.name))

    def Brain(self):
        print("[+] {} : By default, my brain consist of digital circuit".format(self.name))

    def SayMyName(self):
        print("[+] My name is {}".format(self.name))

class Johnny5(Robot):
    def __init__(self, name):
        self.name = name

    def Steering(self):
        print("[+] {} : By default, my steering is classic skid steering".format(self.name))

    def Brain(self):
        print("[+] {} : By default, my brain consist of analog circuit". format(self.name))

    def SayMyName(self):
        print("[+] My name is {}".format(self.name))

walle = WallE('wall-e')
johnny5 = Johnny5('johnny5')

walle.SayMyName()
johnny5.SayMyName()

walle.Steering()
johnny5.Steering()

walle.Brain()
johnny5.Brain()
