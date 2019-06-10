#!/usr/bin/env python3
'''
list_sample.py
sample source code for python training
at jasaplus.com
'''
from os import listdir, walk

def listdir_test(dirname):
    return [f for f in listdir(dirname)]

def oswalk_sample(dirname):
    return [f[0] for f in walk(dirname)]

if __name__ == "__main__":
    dirname = "/tmp"
    list1 = listdir_test(dirname)
    list2 = oswalk_sample(dirname)
    for f in list2:
        print(f)
    print("=" * 166)
    for f in list1:
        print(f)
