#!/usr/bin/python3
'''
client.py
Sample tcp client for python course material on www.jasaplus.com
'''
import socket, time
host = "127.0.0.1"
port = 1337
data = "client message"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    response = sock.recv(4096)
    if response:
        print("[+] From Server : ", repr(response.decode('utf-8')))
    sock.sendall(data.encode('utf-8'))
    time.sleep(2)
sock.close()
