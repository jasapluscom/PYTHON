#!/usr/bin/env python3
'''
isfile_sample.py
check whether a file exists or not for course training
at www.jasaplus.com
'''
import os

if __name__ == "__main__":
    try:
        full_path = "filename.txt"
        if os.path.isfile(full_path):
            print("exists !")
        else:
            print("not found")
    except:
        raise
