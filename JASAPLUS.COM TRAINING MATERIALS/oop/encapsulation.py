#!/usr/bin/env python3
'''
python encapsulation example
made by antonius ringlayer
for python3 training material
at www.jasaplus.com
'''
class Capsule:
    def __init__(self):
        self.data1 = "data 1"
        self.__data2 = "data 2"

    def DoItinMyOwnClass(self):
        print("data1 : " + self.data1)
        print("__data2 : " + self.__data2)
        self.__PrivateMethod()

    def GetterMethod(self):
        return self.data1, self.__data2

    def SetterMethod(self, val1, val2):
        self.data1 = val1
        self.__data2 = val2

    def PublicMethod(self):
        print("I am public method")

    def __PrivateMethod(self):
        print("This is a private method")

capsul = Capsule()
capsul.PublicMethod()
capsul._Capsule__PrivateMethod()

#getter method
get1,get2 = capsul.GetterMethod()
print("data1 from getter method : {}".format(get1))
print("data2 from getter method : {}".format(get2))

#setter method
capsul.SetterMethod("changed 1", "changed 2")
get1,get2 = capsul.GetterMethod()
print("data1 from getter method : {}".format(get1))
print("data2 from getter method : {}".format(get2))

#we can access private variable and call private method within class
#here is the demo :
capsul.DoItinMyOwnClass()
