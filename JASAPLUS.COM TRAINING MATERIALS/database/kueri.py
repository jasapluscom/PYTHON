#!/usr/bin/python3
'''
kueri.py
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
    sql = "show tables"
    cur = _kueri(con, sql)
    rows = cur.fetchone()
    print(rows)
