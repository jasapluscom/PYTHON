#!/usr/bin/env python3
'''
global_local.py
sample source code for python training
at jasaplus.com
'''
globalone = "hello"
globalnum = 77

def myfunc():
    globalone = "wtf"
    print("globalone : "  + globalone)
    print("globalnum : ", globalnum)
    hack = "200"
    print(hack)

def defglo():
    global hack
    hack = "123"

if __name__ == "__main__":
    defglo()
    myfunc()
