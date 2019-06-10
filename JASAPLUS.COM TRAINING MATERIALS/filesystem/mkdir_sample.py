#!/usr/bin/env python3
'''
mkdir_sample.py
sample create directory for course training
at www.jasaplus.com
'''
import os

if __name__ == "__main__":
    try:
        if os.path.isdir("directoryname") == False:
            os.mkdir("directoryname")
    except:
        raise
