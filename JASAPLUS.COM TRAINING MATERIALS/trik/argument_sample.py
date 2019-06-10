#!/usr/bin/env python3
'''
sample argument processing demo
for python3 course at jasaplus.com
'''
import sys
print("\n\tType of sys.argv : " , type(sys.argv))
print("\n\tLength of sys.argv : ", len(sys.argv))
print("\n\tPrinting each argument :")
i = 0
for x in sys.argv:
    print("\n\tsys.argv[" + str(i).strip() +  "] is : " + sys.argv[i])
    i+=1
