#!/usr/bin/env python3
'''
if_else_sample.py
sample if else conditional for course training
at www.jasaplus.com
'''

b = 100

def ifSample(a):
    global b
    if a > b :
        print("a larger than b")
    else:
        print("b larger than a")



if __name__ == "__main__":
    ifSample(200)
    ifSample(90)
