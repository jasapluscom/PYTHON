#!/usr/bin/env python3
'''
sample method overloading
made by Antonius Ringlayer
www.jasaplus.com - www.ringlayer.com

by default method overloading is not supported in python.
We use default value for parameter to create a method that can be
called without parameter or with parameter
since we have supplied default parameter value when
there's no parameter supplied
'''

#prepare new class
class MoDemo():
    def MyPublicMethod(self, data=None):
        if data != None:
            print("[+] data : {}".format(data))
        else:
            print("[+] do nothing")

obj = MoDemo()
obj.MyPublicMethod()
#call it different way : 
obj.MyPublicMethod("hack")
