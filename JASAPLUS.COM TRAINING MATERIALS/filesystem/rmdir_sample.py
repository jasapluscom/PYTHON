#!/usr/bin/env python3
'''
rmdir_sample.py
sample remove a directory for course training
at www.jasaplus.com
'''
import os

if __name__ == "__main__":
    try:
        if os.path.isdir("directoryname"):
            os.rmdir("directoryname")
    except:
        raise
