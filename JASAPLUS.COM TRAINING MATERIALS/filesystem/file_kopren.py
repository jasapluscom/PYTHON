#!/usr/bin/env python3
'''
file_kopren.py
copy file and rename file sample
material for course training
at www.jasaplus.com
'''
import os
from shutil import copyfile, copyfileobj, copy2

def CopyFile(fname):
    try:
        print("[+] copy file using shutil.copyfile()")
        fname_copied = "copyfile_" + fname
        copyfile(fname, fname_copied)
        print("[+] copyfile() done !")
    except:
        raise

def CopyFileObj(fname):
    try:
        print("[+] copy file using shutil.copyfileobj()")
        fname_copied = "copyfileobj_" + fname
        bufsize = 16 * 1024
        with open(fname, 'rb') as src:
            with open(fname_copied, 'wb') as dest:
                copyfileobj(src, dest, bufsize)
        print("[+] copyfileobj() done !")
    except:
        raise

def Copy2(fname):
    try:
        print("[+] copy file using shutil.copy2()")
        fname_copied = "copy2_" + fname
        copy2(fname, fname_copied)
        print("[+] copy2() done !")
    except:
        raise


if __name__ == "__main__":
    fname = input("\ntype file name to copy:").strip()
    CopyFile(fname)
    CopyFileObj(fname)
    Copy2(fname)
