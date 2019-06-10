#!/usr/bin/env python3

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

if __name__ == "__main__":
    print("[+] start")
    wall_e = Robot()
    wall_e.Steering()
    wall_e.MyProperties()
    wall_e.DoIdle()
    wall_e.Head._turn_left()
    wall_e.Head._turn_right()
    wall_e.Arm._pick_object()
    wall_e.Arm._push_object()
