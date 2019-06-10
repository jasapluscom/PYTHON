#!/usr/bin/env python3
'''
aimlbot.py

sample for python3 training at jasaplus.com
'''

import aiml
kernel = aiml.Kernel()
kernel.learn("computers.aiml")
while True:
    print (kernel.respond(input("Enter message : ")))
