#!/usr/bin/env python3
'''
global_local3.py
sample correct source code for python training
at jasaplus.com
'''
globalone = "hello"
globalnum = 77

def myfunc():
    global globalone
    print("globalone : "  + globalone)
    print(type(globalone))
    print("globalnum : ", globalnum)
    hack = "200"
    print(hack)
    globalone = "modified"
    print(globalone)

if __name__ == "__main__":
    myfunc()
