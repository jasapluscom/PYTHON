#!/usr/bin/env python3
'''
flask2.py

sample flask for python3 training
www.jasaplus.com
www.ringlayer.com
'''

from flask import Flask
app = Flask(__name__)

#register a decorator for uri : /
@app.route("/")
def hello():
    return "Main Page"

#register a decorator for uri : /jasaplus
@app.route("/jasaplus")
def ProcJasaplus():
    return "<a href='https://www.jasaplus.com'>Go to Jasaplus</a>"

#register a decorator for uri : /ringlayer
@app.route("/ringlayer")
def ProcRing():
    return "<a href='https://www.ringlayer.com'>Go to Ringlayer</a>"

if __name__ == "__main__":
    app.run(port=1337)
