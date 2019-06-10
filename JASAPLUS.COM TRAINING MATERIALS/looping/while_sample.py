#!/usr/bin/env python3
'''
while_sample.py
sample while for python training
at www.jasaplus.com
'''

def repeatme():
    print("repeated")

if __name__ == "__main__":
    start = 1
    max = 10
    while (start < max):
        print("current start : ", start)
        repeatme()
        start += 1
