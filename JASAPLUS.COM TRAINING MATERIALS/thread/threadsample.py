#!/usr/bin/python3
'''
threadsample.py
Sample multihreading application for python course material on www.jasaplus.com
'''
import threading, socket, time

def task(host, port):
    try:
        data = "GET / HTTP/1.1\r\nHost: " + host + ":80\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0\r\nConnection: keep-alive\r\n\n"
        print("[+] connect to " + host + " on port", port)
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.sendall(data.encode('utf-8'))
        resp = sock.recv(4096)
        if resp:
            print("[+] From Server : ", repr(resp.decode('utf-8')))
    except:
        raise

if __name__ == "__main__":
    print("[+] python3 multi threading sample")
    threadlists = []
    hosts = ["ringlayer.com","jasaplus.com"]
    t1 = threading.Thread(target=task, args=(hosts[0], 80))
    threadlists.append(t1)
    t2 = threading.Thread(target=task, args=(hosts[1], 80))
    threadlists.append(t2)
    for TheThread in threadlists:
        TheThread.start()

    for TheThread in threadlists:
        TheThread.join()
