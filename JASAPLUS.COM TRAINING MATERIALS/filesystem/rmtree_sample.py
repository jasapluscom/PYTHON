#!/usr/bin/env python3
'''
rmtree_sample.py
sample remove a non empty directory for course training
at www.jasaplus.com
'''
import os, shutil

if __name__ == "__main__":
    try:
        if os.path.isdir("non_empty_dir"):
            shutil.rmtree("non_empty_dir")
    except:
        raise
