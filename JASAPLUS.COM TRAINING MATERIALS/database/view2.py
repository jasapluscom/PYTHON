#!/usr/bin/python3
'''
view2.py
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
    sql = "select * from `books`"
    cur = _kueri(con, sql)
    rows = cur.fetchall()
    print(type(rows))
    for row in rows:
        print(row[1])
        print(type(row))
