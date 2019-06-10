#!/usr/bin/env python3
'''
nested_if_sample.py
sample nested if conditional for course training
at www.jasaplus.com
'''

if __name__ == "__main__":
    orignum = 100
    word1 = "ab"
    word2 = "cd"
    word3 = "ef"
    given_number = int(input("type a number : ").strip())
    given_word = input("type a word : ").strip()
    if given_number > orignum:
        #nested if
        if given_word == word1:
            print("correct")
        elif given_word == word2:
            print("nearly correct")
        elif given_word == word3:
            print("nearly incorrect")
        else:
            print("fatal error ! program can't continue")
    else:
        print("fatal error ! application crash !")
