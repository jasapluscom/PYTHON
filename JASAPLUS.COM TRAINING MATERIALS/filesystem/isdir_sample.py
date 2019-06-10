#!/usr/bin/env python3
'''
isdir_sample.py
sample checking whether a directory exists or not for course training
at www.jasaplus.com
'''
import os

if __name__ == "__main__":
    try:
        if os.path.isdir("directoryname"):
            print("exists")
        else:
            print("not found")
    except:
        raise
