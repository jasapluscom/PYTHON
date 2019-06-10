#!/usr/bin/python3
'''
tutup.py
Sample mysql database connection for python course material on www.jasaplus.com
'''
import pymysql

def _konek():
    try:
        con = pymysql.connect('localhost', 'root', '', 'pymysql1')
        return con
    except:
        raise
if __name__ == "__main__":
    con = _konek()
    print("connected to database")
    print("closing connection ... ")
    con.close()
