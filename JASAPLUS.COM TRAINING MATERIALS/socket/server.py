#!/usr/bin/python3
'''
server.py
Sample tcp server for python course material on www.jasaplus.com
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "127.0.0.1"
port = 1337
s.bind((host, port))
print("listening on ", port)
s.listen()
conn,addr = s.accept()
print("Got connection from" + str(addr))
while True:
   msg = 'Server Message'+ "\n"
   conn.send(msg.encode('ascii'))
   request = conn.recv(4096)
   if request:
       print("[+] Message from client : ", repr(request.decode('utf-8')))
conn.close()
