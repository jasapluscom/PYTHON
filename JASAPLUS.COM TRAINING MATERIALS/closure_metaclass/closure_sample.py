#!/usr/bin/env python3
'''
sample python closure for python training
at www.jasaplus.com
'''
def func1(a):
    def func2():
        print(a)
    return func2
obj = func1("remember me")
obj()
