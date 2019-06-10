#!/usr/bin/env python3
'''
file_del.py
deleting file
material for course training
at www.jasaplus.com
'''
import os

if __name__ == "__main__":
    fname = input("\ntype file path that will be removed :").strip()
    if (len(fname) > 0):
        if os.path.isfile(fname):
            os.remove(fname)
            if os.path.isfile(fname):
                print("[-] failed to delete file")
            else:
                print("[+] file deleted successfully")
        else:
            print("file not exists !")
    else:
        print("[-] no file specified")
