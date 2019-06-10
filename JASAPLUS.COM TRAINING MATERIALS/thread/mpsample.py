#!/usr/bin/python3
'''
threadsample.py
Sample multihreading application for python course material on www.jasaplus.com
'''
import multiprocessing, psutil, time, os

def PsutilRoutines():
    try:
        while True:
            print("[+] cpu usage percent:", psutil.cpu_percent(interval=1.0))
            time.sleep(1.5)
            process = psutil.Process(os.getpid())
            print("[+] memory usage percent:", process.memory_percent())
            time.sleep(1.5)
            print(psutil.sensors_battery())
            time.sleep(1.5)
    except:
        raise

def PointLessRoutines(param):
    while True:
        print("hi I'm pointless routine, I got param : " + param)
        time.sleep(1)

if __name__ == "__main__":
    print("[+] python3 multi processing sample")
    processes = []
    for start in range(2):
        proc = multiprocessing.Process(target=PointLessRoutines, args=(str(start),))
        processes.append(proc)
        proc.start()
    proc_cpu = multiprocessing.Process(target=PsutilRoutines)
    processes.append(proc_cpu)
    proc_cpu.start()
