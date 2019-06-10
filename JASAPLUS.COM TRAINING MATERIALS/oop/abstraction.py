#!/usr/bin/env python3
'''
sample abstract class
for python3 training
at www.jasaplus.com
'''

from abc import ABC, abstractmethod

class Robot(ABC):
    @abstractmethod
    def Steering(self):
        pass

    @abstractmethod
    def GenericOperation(self):
        pass

#inheritance 1
class WallE(Robot):
    def Steering(self):
        print("[+] skid steering")

    def GenericOperation(self):
        print("[+] remove trash")



#inheritance 2
class Jibo(Robot):
    def Steering(self):
        print("[+] no steering")

    def GenericOperation(self):
        print("[+] joking")


#instantiations
print("=JIBO BORN=")
jibo = Jibo()
jibo.Steering()
jibo.GenericOperation()

print("\n=WALL-E BORN=")
walle = WallE()
walle.Steering()
walle.GenericOperation()
