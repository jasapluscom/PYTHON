#!/usr/bin/env python3
'''
created by Antonius Ringlayer
material for python3 course
'''
#parent class :
class Robot():
    sound = "?"
    steering = "?"
    name = "?"

    def __init__(self):
        self.sound = "beep"
        self.name = "wall e"

    def Steering(self):
        self.steering = "skid steering"

    def DoIdle(self):
        print("[+] do nothing")

    def MyProperties(self):
        print("[+] sound : " + self.sound)
        print("[+] steering : " + self.steering)
        print("[+] name : " + self.name)

    class Head:
        def _turn_left():
            print("[+] robot head turn left")
        def _turn_right():
            print("[+] robot head turn right")

    class Arm:
        def _pick_object():
            print("[+] robot arm pick object")
        def _push_object():
            print("[+] robot arm push object")

#inheritance class :
class ThreeWheeledRobot(Robot):
    def __init__(self):
        self.sound = "squeeze"
        self.name = "differential drive robot"
        self.steering = "differential drive"

    #method override
    def DoIdle(self):
        print("[+] idle override")

    def AdditionalMethod(self):
        print("[+] Hello I have new method")


#instantiation

bot = ThreeWheeledRobot()
bot.MyProperties()
bot.DoIdle()
bot.AdditionalMethod()
bot.Head._turn_left()
bot.Arm._pick_object()
