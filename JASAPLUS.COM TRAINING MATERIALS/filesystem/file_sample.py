#!/usr/bin/env python3
'''
file_sample.py
- create new file
- write file content
- read file
- append file content
- read file
material for course training
at www.jasaplus.com
'''
def create_write_file(file_path):
    try:
        print("[+] writing new file : " + file_path)
        with open(file_path, 'w') as fp:
            fp.write("write new file content\n")
    except:
        raise

def read_file(file_path):
    try:
        print("[+] reading file content : " + file_path)
        with open(file_path, 'r') as fp:
            data = fp.read()
            print("file content : \n")
            print(data)
    except:
        raise

def append_file(file_path):
    try:
        print("[+] appending file content : " + file_path)
        with open(file_path, 'a+') as fp:
            fp.write("\nappended text\n")
    except:
        raise

if __name__ == "__main__":
    file_path = "sample.txt"
    create_write_file(file_path)
    input("\npress any key to continue reading file")
    read_file(file_path)
    input("\npress any key to continue append file content")
    append_file(file_path)
    input("\npress any key to continue reading file")
    read_file(file_path)
