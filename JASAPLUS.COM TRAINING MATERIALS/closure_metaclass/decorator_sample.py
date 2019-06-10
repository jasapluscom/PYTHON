#!/usr/bin/env python3
'''
sample decorator for python training
at www.jasaplus.com
'''
class Robot():
    def SayHello(self):
        print("[+] hello i am robot")

    def func1(self, func):
        def func2():
            print("[+] decorated")
            self.SayHello()
        return func2

robot = Robot()
res = robot.func1(robot.SayHello)
print(type(res))
res()
