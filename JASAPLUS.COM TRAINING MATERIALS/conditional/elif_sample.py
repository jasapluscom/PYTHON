#!/usr/bin/env python3
'''
elif_sample.py
sample elif conditional for course training
at www.jasaplus.com
'''

password1 = "ringlayer"
password2 = "hack"

def Validate_Password(given_password):
    global password1
    global password2
    retme = 0
    if (given_password == password1):
        retme = 1
    elif (given_password == password2):
        retme = 2
    else:
        retme = -1

    return retme

if __name__ == "__main__":
    inputpass = input("password : ")
    result_privilege = Validate_Password(inputpass)
    if result_privilege == 1:
        print("admin privilege")
    elif result_privilege == 2:
        print("operator privilege")
    else:
        print("[-] error ! invalid password !")
