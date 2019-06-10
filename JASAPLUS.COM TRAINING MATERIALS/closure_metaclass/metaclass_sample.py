#!/usr/bin/env python3

'''
metaclass_sample.py
sample metaclass for python3 training
at www.jasaplus.com
'''

#metaclass :
class TheMetaClass:
    #constructor
    def __new__(cls, clsname, superclasses, attributedict):
        try:
            print("[+] __new__")
            print("\t cls : "  + str(cls))
            print("\t clsname : " + str(clsname))
            print("\tattribute dict : " + str(attributedict))
            return super().__new__(cls)
        except:
            raise

    #initializer
    def __init__(self, clsname, superclasses, attributedict):
        try:
            print("[+] __init__")
            print(type(self))
        except:
            raise

    #call
    def __call__(self):
        try:
            print("[+] __call__")
            print(type(self))
        except:
            raise


class FooClass(metaclass=TheMetaClass):
    pass

f = FooClass()
