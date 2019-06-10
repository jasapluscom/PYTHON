#!/usr/bin/env python3
'''
kopren_sample.py
sample source code for python training
at jasaplus.com
'''
import os, shutil

def _copytree(dirname, newdir):
    try:
        print("[+] copytree")
        shutil.copytree(dirname, newdir)
    except:
        raise

def _mkdir(dirname):
    try:
        print("[+] mkdir")
        os.mkdir(dirname)
    except:
        raise

def _rename(dirname, newname):
    try:
        print("[+] rename")
        os.rename(dirname, newname)
    except:
        raise

def _rmdir(dirname):
    try:
        print("[+] rmdir")
        os.rmdir(dirname)
    except:
        try:
            shutil.rmtree(dirname)
        except:
            raise
        pass

def func_kopidir(dirname, newdir):
    try:
        if os.path.isdir(newdir):
            print("[+] already copied before")
        elif os.path.isdir(dirname):
            _copytree(dirname, newdir)
        else:
            _mkdir(dirname)
            _copytree(dirname, newdir)
    except:
        raise

def func_rendir(dirname, newname):
    try:
        if (os.path.isdir(dirname)):
            if (os.path.isdir(newname) == False):
                _rename(dirname, newname)
            else:
                _rmdir(newname)
                _rename(dirname, newname)
        else:
            print("[-] directory {} not exists ... creating directory {} ".format(dirname, dirname))
            _mkdir(dirname)
            if (os.path.isdir(newname) == False):
                _rename(dirname, newname)
            else:
                _rmdir(newname)
                _rename(dirname, newname)
    except:
        raise

if __name__  == "__main__" :
    dirname = "test"
    newdir = "copied"
    newname = "changed"
    func_kopidir(dirname, newdir)
    func_rendir(dirname, newname)
