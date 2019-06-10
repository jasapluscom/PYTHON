#!/usr/bin/env python3
'''
operator_overloading.py
sample operator overloading in class
python training material for jasaplus.com
'''

class Operation:
    def __init__(self, val):
        self.val = val

    def __add__(self, obj):
        return (self.val + obj.val - 1)

    def __sub__(self, obj):
        return self.val - obj.val

res1 = Operation(10)
res2 = Operation(5)

print(res1 + res2)

res3 = Operation(10)
res4 = Operation(5)

print(res1 - res2)
