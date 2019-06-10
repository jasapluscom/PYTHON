#!/usr/bin/python3
'''
update.py
Sample mysql database connection and query for python course material on www.jasaplus.com
'''
import pymysql

def _konek():
    try:
        con = pymysql.connect('localhost', 'root', '', 'pymysql1')
        return con
    except:
        raise

def _kueri(con,sql):
    try:
        with con:
            cur = con.cursor()
            cur.execute(sql)
            return cur
    except:
        raise

if __name__ == "__main__":
    con = _konek()
    print("connected to database")
    sql = "update `books` set `title` = 'New Title' where `id` like '4'"
    cur = _kueri(con, sql)
