#!/usr/bin/env python3
'''
lambda samples
for python3 course at jasaplus.com
'''

#sample lambda1
f = lambda x: x+10
print(f(1))
print(f(2))
print(type(f))

#sample lambda2
f2 = lambda a, b: a+b
print(f2(1, 2))
print(f2(3, 4))
print(type(f2))

#sample lambda2
f3 = lambda a: print(a)
f3("lambda sample")
print(type(f3))
