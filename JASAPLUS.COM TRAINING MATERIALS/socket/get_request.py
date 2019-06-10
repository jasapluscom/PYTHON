#!/usr/bin/env python3
'''
sample http get request client for python training course
at www.jasaplus.com
'''
import socket
target_host = "www.phrack.org"
target_port = 80
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.connect((target_host,target_port))
request = "GET /index.html HTTP/1.1\r\nHost: www.phrack.org\r\n\r\n"
sockfd.sendall(request.encode())
full_source = ""
response = sockfd.recv(4096)
while True:
    full_source += repr(response)
    response = sockfd.recv(4096)
    if not response:
        break
print("http response : \n\n%s", full_source)
