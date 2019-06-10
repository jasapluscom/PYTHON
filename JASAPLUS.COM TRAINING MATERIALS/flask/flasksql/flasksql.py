#!/usr/bin/env python3
'''
flaskweb.py

sample flask for python3 training
www.jasaplus.com
www.ringlayer.com
'''
import pymysql
from flask import Flask, render_template
app = Flask(__name__)

#start global default vars
HeaderAbout = "about"
ContainerAbout = "welcome to about"

HeaderKontak = "contact"
ContainerKontak= "welcome to contact"

HeaderPortfolio = "portfolio"
ContainerPortfolio = "welcome to portfolio"
#eof global default vars

def _konek():
    try:
        con = pymysql.connect('localhost', 'root', '', 'flask')
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

def _get_all_page():
    try:
        global HeaderAbout,ContainerAbout, HeaderKontak, ContainerKontak, HeaderPortfolio, ContainerPortfolio
        con = _konek()
        sql = "select header, container, mode from `page`"
        cur = _kueri(con, sql)
        rows = cur.fetchall()
        for row in rows:
            cur_header = row[0]
            cur_container = row[1]
            cur_mode = row[2]
            if cur_mode == "about":
                HeaderAbout = cur_header
                ContainerAbout = cur_container
            elif cur_mode == "kontak":
                HeaderKontak = cur_header
                ContainerKontak = cur_container
            elif cur_mode == "portfolios":
                HeaderPortfolio = cur_header
                ContainerPortfolio = cur_container
    except:
        raise

#register a decorator for uri : /
@app.route("/")
def Home():
    header = "Home"
    container = "Welcome to my Home"
    return render_template("index.html", header_home=header, container_home=container)

#register a decorator for uri : /about
@app.route("/about")
def About():
    return render_template("about.html", header_about = HeaderAbout , container_about = ContainerAbout)

#register a decorator for uri : /contact
@app.route("/contact")
def Contact():
    return render_template("contact.html", header_contact = HeaderKontak, container_contact = ContainerKontak)

#register a decorator for uri : /contact
@app.route("/portfolio")
def Portfolio():
    return render_template("portfolio.html", header_portfolio = HeaderPortfolio, container_portfolio = ContainerPortfolio)

if __name__ == "__main__":
    _get_all_page()
    app.run(port=8888)
